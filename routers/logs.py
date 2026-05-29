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

@router.put("/logs/{log_id}")
def update_log(log_id: int, log: LogItem):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE logs
        SET title=?, content=?, author=?
        WHERE id=?
        """,
        (log.title, log.content, log.author, log_id)
    )

    conn.commit()

    if cursor.rowcount == 0:

        conn.close()

        raise HTTPException(
            status_code=404,
            detail="日志不存在"
        )

    conn.close()

    return {
        "message": "日志更新成功"
    }

@router.delete("/logs/{log_id}")
def delete_log(log_id: int):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM logs WHERE id = ?",
        (log_id,)
    )

    if cursor.rowcount == 0:

        conn.close()

        return {
            "error": "日志不存在"
        }

    conn.commit()

    conn.close()

    return {
        "message": "日志删除成功"
    }

@router.put("/logs/{log_id}")
def update_log(log_id: int, log: UpdateLogItem):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE logs
        SET title = ?, content = ?, author = ?
        WHERE id = ?
        """,
        (
            log.title,
            log.content,
            log.author,
            log_id
        )
    )

    conn.commit()

    conn.close()

    return {
        "message": "日志更新成功"
    }