# 🚗 OLX AutoSale Parser & AutoPoster

**A fully automated system for mass posting ads on OLX using product data from an external store**


## ⚠️ Disclaimer
This project is provided strictly for educational and research purposes only.
The author does not encourage or endorse automated posting, scraping, or any activity that violates OLX’s Terms of Service or local laws.
Use responsibly and at your own risk. (I know I forgot to add .env in the first 3 commits, my bad)

---

## 🧩 Project Overview

This project combines two powerful components:

- A **product data parser** that pulls listings from an external store API  
- An **OLX auto-poster** that publishes ads using a real Chrome profile

The system is fully autonomous: it fetches product data, cleans descriptions, downloads images, calculates prices, and posts ads to OLX using a stealth-masked browser.

---

## ⚙️ Project Structure

```
Parser-AutoPostOLX/
├── .env                      # API and image URL configuration
├── auto_sale.py             # OLX auto-poster logic
├── parser.py                # Product data parser
├── stealth_driver.py        # Chrome setup with stealth masking
├── main.py                  # Entry point: parsing + posting
├── foto/                    # Folder for product images
├── ChromeProfile/           # Browser profile for OLX
└── README.md                # Project documentation
```

---

## 🔍 Product Parser (`parser.py`)

- Loads JSON data from `SHOP_API_URL`
- Extracts:
  - Product name
  - Cleaned description (HTML → plain text)
  - Original price
  - Custom “middle” price (auto-calculated)
  - Main product image
- Saves image to `foto/foto1.png`
- Uses a generator for efficient streaming

---

## 🤖 OLX Auto-Poster (`auto_sale.py`)

- Uses `undetected_chromedriver` with a real Chrome profile
- Masks Selenium to bypass OLX bot detection
- Automatically fills:
  - Title
  - Description
  - Item condition
  - Price
  - Delivery options (InPost, Ruch, DpD)
  - Image upload
- Keeps browser open for manual review before submission

---

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   **Python version: 3.8 – 3.11 supported**<br><br>

2. Configure `.env`:
   ```
   SHOP_API_URL=https://example.com/api/item/
   SHOP_IMG_URL=https://example.com/media/images/
   ```

3. Run the main script:
   ```bash
   python main.py
   ```

---

## 🛡️ Stealth & Stability

- Uses `undetected_chromedriver` with key flags:
  - `--disable-blink-features=AutomationControlled`
  - `--no-first-run`, `--no-default-browser-check`
  - `--user-data-dir` and `--profile-directory` for real browser identity
- This setup ensures stable, bot-free posting on OLX
