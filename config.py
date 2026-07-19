import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")

APP_NAME = os.getenv("APP_NAME")

VERSION = os.getenv("VERSION")

DEFAULT_PAGE_SIZE = 5

MAX_PAGE_SIZE = 50

LOG_FILE = "app.log"