from bot.logging_config import setup_logger

setup_logger()  


from flask import Flask, render_template, request
from bot.client import BinanceClient
from bot.orders import OrderManager

app = Flask(__name__)

# Init Binance
binance = BinanceClient()
client = binance.client   # <-- IMPORTANT (no get_client())

order_manager = OrderManager(client)

SYMBOLS = ["BTCUSDT", "ETHUSDT"]


@app.route("/", methods=["GET", "POST"])
def index():

    order_data = None
    error = None

    if request.method == "POST":

        try:
            symbol = request.form["symbol"]
            side = request.form["side"]
            order_type = request.form["type"]
            quantity = float(request.form["quantity"])

            price = request.form.get("price")
            price = float(price) if price else None

            # Place order
            order = order_manager.place_order(
                symbol,
                side,
                order_type,
                quantity,
                price
            )

            # Extract values
            order_data = {
                "id": order.get("orderId"),
                "status": order.get("status"),
                "executed": order.get("executedQty"),
                "avg_price": order.get("avgPrice")
            }

        except Exception as e:
            error = str(e)

    return render_template(
        "index.html",
        symbols=SYMBOLS,
        order=order_data,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
