from database_manager import get_connection




def get_all_logs(page: int, size: int):

    conn = get_connection()

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

    conn = get_connection()
    
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

    conn = get_connection()

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

def add_log(
    title,
    content,
    author,
    created_at
):

    conn = get_connection()

    cursor = conn.cursor()

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
            title,
            content,
            author,
            created_at
        )
    )

    conn.commit()

    conn.close()

def update_log(
    log_id,
    title,
    content,
    author
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE logs
        SET
            title=?,
            content=?,
            author=?
        WHERE id=?
        """,
        (
            title,
            content,
            author,
            log_id
        )
    )

    conn.commit()

    affected = cursor.rowcount

    conn.close()

    return affected


def delete_log(log_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM logs
        WHERE id=?
        """,
        (log_id,)
    )

    conn.commit()

    affected = cursor.rowcount

    conn.close()

    return affected

def search_logs(keyword):

    conn = get_connection()

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

    return logs


def get_author_stats():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT author,
               COUNT(*)
        FROM logs
        GROUP BY author
        """
    )

    result = cursor.fetchall()

    conn.close()

    return result