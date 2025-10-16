# 🦾 Binance Futures Testnet Trading Bot

A simplified **Python trading bot** built for the **Binance Futures Testnet (USDT-M)**.  
It supports **Market**, **Limit**, and **Stop-Limit** orders with **Buy/Sell** options via a command-line interface (CLI).  
Includes complete **logging**, **error handling**, and an optional **TWAP (Time-Weighted Average Price)** strategy.

---

## 🚀 Features

✅ Place **Market** and **Limit** orders  
✅ Supports **Buy** and **Sell** sides  
✅ Uses **Binance Futures Testnet REST API**  
✅ Interactive **Command-Line Interface (CLI)**  
✅ Comprehensive **logging & error handling**  
✅ **Stop-Limit** advanced order type (Bonus)  
✅ Optional **TWAP (algorithmic)** order support  
✅ Modular, reusable design with clean structure  

---

## 📁 Project Structure

```

trading_bot/
├── bot.py             # Core trading logic
├── cli.py             # Command-line interface
├── logger.py          # Logging configuration
├── requirements.txt   # Dependencies
├── README.md          # Documentation
└── trading_bot.log    # Example runtime logs

````

---

## ⚙️ Installation

### 1. Clone or Download

```bash
git clone https://github.com/<yourusername>/binance-futures-bot.git
cd binance-futures-bot/trading_bot
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Register Testnet Account

1. Go to [Binance Futures Testnet](https://testnet.binancefuture.com).
2. Create an account and enable **Futures**.
3. Generate **API Key** and **Secret Key** from your Testnet profile.
4. Make sure permissions for **Enable Futures** and **Enable Trading** are active.

---

## ▶️ Usage

Run the CLI:

```bash
python cli.py
```

Example run:

```
=== Binance Futures Trading Bot CLI ===
Enter Binance API Key: ********
Enter Binance API Secret: ********

Options: [1] Place Order [2] Check Balance [3] Exit
Choose option: 1
Symbol (e.g., BTCUSDT): BTCUSDT
Buy/Sell: buy
Order Type (market/limit/stop-limit): market
Quantity: 0.001
```

---

## 🧠 Bonus: TWAP Order Type (Optional)

You can execute a **TWAP strategy** (Time-Weighted Average Price) to simulate algorithmic trading.

Example:

```
Options: [4] TWAP Order
Symbol (e.g., BTCUSDT): BTCUSDT
Buy/Sell: buy
Total Quantity: 0.005
Number of chunks: 5
Delay between chunks (sec): 10
```

This splits your total order into smaller market orders spaced by the delay.

---

## 🧾 Logging

All API requests, responses, and errors are recorded in:

```
trading_bot.log
```

Example log snippet:

```
2025-10-16 18:42:03 - INFO - Order placed successfully: {'symbol': 'BTCUSDT', 'orderId': 12345678, ...}
2025-10-16 18:42:05 - INFO - Fetched account balance
```

---

## 🧱 Tech Stack

* **Language:** Python 3.x
* **Libraries:** `python-binance`, `pandas`
* **API:** Binance Futures Testnet REST API
* **Interface:** Command-line (CLI)

---

## ⚡ Example Output

```text
Order executed:
{
  "symbol": "BTCUSDT",
  "orderId": 9824513,
  "type": "MARKET",
  "side": "BUY",
  "status": "FILLED",
  "executedQty": "0.001",
  "avgPrice": "67123.50"
}
```

---

## 💾 Requirements File

`requirements.txt`

```
python-binance==1.0.16
pandas
```
