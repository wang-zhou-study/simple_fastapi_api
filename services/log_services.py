import sqlite3

DB_NAME = "logs.db"


def get_all_logs(page: int, size: int):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    offset = (page - 1) * size

    cursor.execute(
        """
        SELECT * FROM logs
        LIMIT ? OFFSET ?
        """,
        (size, offset)
    )

    logs = cursor.fetchall()

    conn.close()

    return logs


def get_log_by_id(log_id: int):

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

    return log


def get_total_logs():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM logs
        """
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total