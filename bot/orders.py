import logging
from binance.exceptions import BinanceAPIException


class OrderManager:

    def __init__(self, client):
        self.client = client

    def place_order(self, symbol, side, order_type, quantity, price=None):

        try:

            logging.info(f"Placing order: {symbol} {side} {order_type}")

            if order_type == "MARKET":

                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="MARKET",
                    quantity=quantity
                )

            else:

                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="LIMIT",
                    timeInForce="GTC",
                    quantity=quantity,
                    price=price
                )

            logging.info(f"Order Success: {order}")

            return order

        except BinanceAPIException as e:

            logging.error(f"Binance API Error: {e}")
            raise

        except Exception as e:

            logging.error(f"General Error: {e}")
            raise
