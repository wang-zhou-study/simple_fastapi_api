import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    encoding="utf-8",
    format="%(asctime)s - %(levelname)s - %(message)s"
)