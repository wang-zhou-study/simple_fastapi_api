import sqlite3

DB_NAME = "logs.db"


def get_connection():

    return sqlite3.connect(DB_NAME)