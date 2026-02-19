import logging


def setup_logger():

    log_file = "bot.log"

    # Remove old handlers (important for Flask auto-reload)
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler()
        ]
    )

    # Silence noisy libraries
    logging.getLogger("werkzeug").setLevel(logging.ERROR)
    logging.getLogger("flask").setLevel(logging.ERROR)
    logging.getLogger("urllib3").setLevel(logging.ERROR)
