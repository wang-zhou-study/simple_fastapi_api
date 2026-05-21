import sqlite3
from fastapi import APIRouter, HTTPException
from models.log_model import LogItem

router = APIRouter()

DB_NAME = "logs.db"



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

@router.get("/logs/{log_id}")
def get_log(log_id: int):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM logs WHERE id=?",
        (log_id)
    )

    log = cursor.fetchone()

    conn.close()

    if log is None:

        raise HTTPException(
            status_code=404,
            detail="日志不存在"
        )
    
    return{
        "log": log
    }