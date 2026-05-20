import sqlite3
from fastapi import APIRouter
from models.log_model import LogItem

router = APIRouter()

DB_NAME = "logs.db"


print("logs.py loaded")

@router.post("/logs")
def add_log(log: LogItem):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO logs (title, content, author)
        VALUES (?, ?, ?)
        """,
        (log.title, log.content, log.author)
    )

    conn.commit()
    conn.close()

    return {
        "message": "日志添加成功"
    }


@router.get("/logs")
def get_logs():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM logs")

    logs = cursor.fetchall()

    conn.close()

    return {
        "logs": logs
    }