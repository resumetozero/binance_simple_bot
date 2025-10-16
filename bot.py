from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException, BinanceOrderException
from logger import setup_logger
from time import time, sleep

logger = setup_logger()

class TradingBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.testnet = testnet
        self.client = Client(api_key, api_secret, testnet=testnet)
        if testnet:
            self.client.API_URL = 'https://testnet.binancefuture.com/fapi/v1'
        logger.info("TradingBot initialized. Testnet: %s", testnet)


    def place_twap_order(self, symbol, side, total_qty, intervals, delay, order_type='market'):
        """
        Places multiple small market orders spaced by 'delay' seconds.
        Example: TWAP of 0.1 BTC split into 5 chunks every 10s.
        """
        chunk_size = total_qty / intervals
        logger.info(f"Starting TWAP order: {total_qty} {symbol}, {intervals} intervals, {delay}s apart.")

        for i in range(intervals):
            logger.info(f"Placing chunk {i+1}/{intervals}")
            order = self.place_order(symbol, side, order_type, round(chunk_size, 4))
            if order:
                logger.info(f"Chunk {i+1} executed: {order['orderId']}")
            time.sleep(delay)

        logger.info("TWAP execution completed.")


    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            side_enum = SIDE_BUY if side.lower() == 'buy' else SIDE_SELL
            if order_type.lower() == 'market':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side_enum,
                    type=ORDER_TYPE_MARKET,
                    quantity=quantity
                )
            elif order_type.lower() == 'limit':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side_enum,
                    type=ORDER_TYPE_LIMIT,
                    timeInForce=TIME_IN_FORCE_GTC,
                    quantity=quantity,
                    price=price
                )
            elif order_type.lower() == 'stop-limit':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side_enum,
                    type=ORDER_TYPE_STOP_LOSS_LIMIT,
                    timeInForce=TIME_IN_FORCE_GTC,
                    quantity=quantity,
                    price=price,
                    stopPrice=stop_price
                )
            else:
                logger.error("Unsupported order type: %s", order_type)
                return None

            logger.info("Order placed successfully: %s", order)
            return order

        except BinanceAPIException as e:
            logger.error("Binance API Exception: %s", e)
        except BinanceOrderException as e:
            logger.error("Binance Order Exception: %s", e)
        except Exception as e:
            logger.error("Unexpected error: %s", e)

    def get_balance(self):
        try:
            balance = self.client.futures_account_balance()
            logger.info("Fetched account balance")
            return balance
        except Exception as e:
            logger.error("Error fetching balance: %s", e)
            return None