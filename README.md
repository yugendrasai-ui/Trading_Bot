# Trading Bot (Binance Futures Testnet)

This project is a simple Binance Futures Testnet trading bot with a web interface built using Flask.  
It allows users to place Market and Limit orders and view order status.

---

## Features

- Place BUY/SELL orders on Binance Futures Testnet
- Web-based UI for easy trading

---

## Folder Structure

Trading_Bot/
│
├── bot/
│   ├── client.py
│   ├── logging_config.py
│   ├── orders.py
│   ├── validators.py
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── .env
├── .gitignore
├── app.py
├── cli.py
├── requirements.txt
├── README.md

---

## Setup Instructions

### 1. Clone the Repository

git clone https://github.com/yugendrasai-ui/Trading-Bot.git  
cd Trading-Bot

---

### 2. Install Dependencies

pip install -r requirements.txt

---

### 3. Configure API Keys

Create a file named .env in the project root.

Trading_Bot/.env

Add your Binance Testnet keys:

API_KEY=your_api_key_here  
API_SECRET=your_api_secret_here

Get keys from:  
https://testnet.binancefuture.com

---

### 4. Run the Application

python app.py

Open in browser:

http://127.0.0.1:5000

---

## How to Use

1. Open browser and go to http://127.0.0.1:5000
2. Select Symbol, Side, Order Type
3. Enter Quantity and Price (for LIMIT)
4. Click Place Order
5. View order result on screen

---

## Run Using CLI (Optional)

python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.002 --price 65000

---

## Logging

All order activity is saved in:

bot.log


---

## Assumptions

- User has Binance Futures Testnet account
- Valid API keys
- Stable internet connection
- For learning and demo purposes only


## Author

Developed by Ugendra Sai