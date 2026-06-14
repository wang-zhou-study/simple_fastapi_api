import logging
import sqlite3

from config import DB_NAME
from datetime import datetime
from fastapi import APIRouter, HTTPException
from models.log_model import LogItem
from fastapi import HTTPException
from services.log_services import (
    get_all_logs,
    get_log_by_id,
    get_total_logs
)
from utils.response import (
    success_response,
    error_response
)

router = APIRouter()



@router.post("/logs")
def add_log(log: LogItem):

    logging.info(f"新增日志: {log.title}")

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    created_at = datetime.now().strftime(
    "%Y-%m-%d %H:%M:%S"
    )

    cursor.execute(
        """
        INSERT INTO logs
        (
            title,
            content,
            author,
            created_at
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            log.title,
            log.content,
            log.author,
            created_at
        )
    )
    conn.commit()
    conn.close()

    return success_response(
        message="日志添加成功"
    )


@router.get("/logs")
def get_logs(page: int = 1, size: int = 5):

    logs = get_all_logs(page, size)

    result = []

    for log in logs:

        result.append(
            {
                "id": log[0],
                "title": log[1],
                "content": log[2],
                "author": log[3],
                "created_at": log[4]
            }
        )

    return success_response(
        data=result
    )

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

    return success_response(
        message="日志更新成功"
    )

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


@router.get("/search")
def search_logs(keyword: str):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM logs
        WHERE title LIKE ?
        """,
        (f"%{keyword}%",)
    )

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
        (log_id,)
    )

    log = cursor.fetchone()

    conn.close()

    if log is None:

        raise HTTPException(
            status_code=404,
            detail="日志不存在"
        )

    return {
        "id": log[0],
        "title": log[1],
        "content": log[2],
        "author": log[3]
    }

@router.get("/logs/{log_id}")
def get_log(log_id: int):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM logs WHERE id=?",
        (log_id,)
    )

    log = cursor.fetchone()

    conn.close()

    if log is None:

        raise HTTPException(
            status_code=404,
            detail="日志不存在"
        )

    return {
        "id": log[0],
        "title": log[1],
        "content": log[2],
        "author": log[3]
    }

@router.get("/stats")
def get_stats():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM logs"
    )

    total_logs = cursor.fetchone()[0]

    cursor.execute(
        """
        SELECT COUNT(DISTINCT author)
        FROM logs
        """
    )

    total_authors = cursor.fetchone()[0]

    conn.close()

    return {
        "total_logs": total_logs,
        "total_authors": total_authors
    }


@router.get("/stats")
def get_stats():

    total = get_total_logs()

    return {
        "total_logs": total
    }

@router.get("/logs/{log_id}")
def get_log(log_id: int):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM logs
        WHERE id = ?
        """,
        (log_id,)
    )

    log = cursor.fetchone()

    conn.close()

    if log is None:

        raise HTTPException(
            status_code=404,
            detail="日志不存在"
        )

    return {
        "id": log[0],
        "title": log[1],
        "content": log[2],
        "author": log[3],
        "created_at": log[4]
    }