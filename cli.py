from bot import TradingBot
from getpass import getpass

def main():
    print("=== Binance Futures Trading Bot CLI ===")
    api_key = "HuNo2fqzP3hfd587aZ8E0YyOhXcnsjYZfdrlYfAR2e0Yd4AkMQKysM0KoITZR6PD"
    # input("Enter your Binance API Key: ").strip()
    api_secret = "xzrEJO9wQt6f0rYFlj9GiytAYUkFsocJI3l3qJnpruDAACqqz3Fife088mYyRl8q"
    # input("Enter your Binance API Secret: ").strip()

    bot = TradingBot(api_key, api_secret, testnet=True)

    while True:
        print("\nOptions: [1] Place Order [2] Check Balance [3] Exit")
        choice = input("Select option: ").strip()

        if choice == "1":
            symbol = input("Symbol (e.g., BTCUSDT): ").strip().upper()
            side = input("Buy/Sell: ").strip().lower()
            order_type = input("Order Type (market/limit/stop-limit): ").strip().lower()
            quantity = float(input("Quantity: "))
            price = None
            stop_price = None
            if order_type in ['limit', 'stop-limit']:
                price = float(input("Price: "))
            if order_type == 'stop-limit':
                stop_price = float(input("Stop Price: "))

            order = bot.place_order(symbol, side, order_type, quantity, price, stop_price)
            if order:
                print("Order executed:", order)

        elif choice == "2":
            balance = bot.get_balance()
            print(balance)

        elif choice == "3":
            print("Exiting CLI...")
            break

        elif choice == "4":
            symbol = input("Symbol (e.g., BTCUSDT): ").strip().upper()
            side = input("Buy/Sell: ").strip().lower()
            total_qty = float(input("Total Quantity: "))
            intervals = int(input("Number of chunks: "))
            delay = float(input("Delay between chunks (sec): "))
            bot.place_twap_order(symbol, side, total_qty, intervals, delay)

        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
