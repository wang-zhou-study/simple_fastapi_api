import logging
import sqlite3

from fastapi import APIRouter, HTTPException
from models.log_model import LogItem

router = APIRouter()

DB_NAME = "logs.db"


@router.post("/logs")
def add_log(log: LogItem):

    logging.info(f"新增日志: {log.title}")

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

    logging.info("获取全部日志")

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM logs")

    logs = cursor.fetchall()

    conn.close()

    return {
        "logs": logs
    }