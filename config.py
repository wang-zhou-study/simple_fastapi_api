import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")

APP_NAME = os.getenv("APP_NAME")

VERSION = os.getenv("VERSION")