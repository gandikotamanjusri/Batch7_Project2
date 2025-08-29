# Batch7_Project2
# 📉 Price Tracker – Python Web Scraper

## 📌 Overview
This project tracks the price of a product from an e-commerce website (e.g., Amazon) and:
- Extracts product **title & price** using BeautifulSoup.
- Saves price history in **CSV**.
- Sends an **email alert** when price drops below a threshold.
- Can be scheduled with cron (Linux) or Task Scheduler (Windows).

---

## ⚙️ Requirements
- Python 3.8+
- Install dependencies:
```bash
pip install requests beautifulsoup4
