import requests
from bs4 import BeautifulSoup
import smtplib
import json
import time

# Load config
with open("config.json", "r") as f:
    config = json.load(f)

URL = config["url"]
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
THRESHOLD = config["threshold_price"]
EMAIL = config["email"]
PASSWORD = config["password"]
TO_EMAIL = config["to_email"]

def check_price():
    try:
        page = requests.get(URL, headers=HEADERS)
        soup = BeautifulSoup(page.content, "html.parser")

        # --- Get Product Title ---
        title_tag = soup.find("span", {"id": "productTitle"})
        if title_tag:
            title = title_tag.get_text().strip()
        else:
            print("⚠️ Could not find product title")
            title = "Unknown Product"

        # --- Get Product Price ---
        price_tag = soup.find("span", {"class": "a-offscreen"})  # Amazon price class
        if price_tag:
            price_str = price_tag.get_text().replace("₹", "").replace(",", "").strip()
            price = float(price_str)
        else:
            print("⚠️ Could not find product price")
            return

        print(f"{title} - Current Price: ₹{price}")

        if price < THRESHOLD:
            send_email(title, price)

    except Exception as e:
        print(f"Error scraping: {e}")

def send_email(title, price):
    try:
        subject = f"Price Drop Alert: {title}"
        body = f"The price dropped to ₹{price}\nCheck here: {URL}"
        message = f"Subject: {subject}\n\n{body}"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, TO_EMAIL, message)
        server.quit()
        print("✅ Email alert sent!")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    while True:
        check_price()
        time.sleep(3600)  # check every 1 hour
