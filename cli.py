import argparse

from bot.client import BinanceClient
from bot.orders import OrderManager
from bot.validators import validate_inputs
from bot.logging_config import setup_logger


def main():

    setup_logger()

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:

        validate_inputs(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n📌 Order Request:")
        print(vars(args))

        client = BinanceClient().client
        manager = OrderManager(client)

        order = manager.place_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n✅ Order Response:")
        print("Order ID:", order["orderId"])
        print("Status:", order["status"])
        print("Executed Qty:", order["executedQty"])
        print("Avg Price:", order.get("avgPrice", "N/A"))

        print("\n🎉 Order placed successfully")

    except Exception as e:

        print("\n❌ Order Failed")
        print("Error:", e)


if __name__ == "__main__":
    main()
