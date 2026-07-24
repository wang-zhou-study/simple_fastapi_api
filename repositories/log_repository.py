"""
repositories/log_repository.py

Repository（仓库层）

这一层只负责：
    1. 查询数据库
    2. 修改数据库
    3. 删除数据库

不要写任何业务逻辑。

企业项目几乎都会有这一层。
"""

from sqlalchemy.orm import Session

from models.log_table import Log


# ==================================================
# 查询所有日志（分页）
# ==================================================
def get_all_logs(
    db: Session,
    page: int,
    size: int
):
    """
    查询日志列表

    参数：
        db      数据库Session
        page    当前页
        size    每页数量

    SQL：

        SELECT *
        FROM logs
        LIMIT size
        OFFSET offset
    """

    # 第几条开始查询
    offset = (page - 1) * size

    logs = (
        db.query(Log)
        .offset(offset)
        .limit(size)
        .all()
    )

    return logs


# ==================================================
# 根据ID查询
# ==================================================
def get_log_by_id(
    db: Session,
    log_id: int
):
    """
    查询单条日志

    SQL：

        SELECT *
        FROM logs
        WHERE id = ?
    """

    return (
        db.query(Log)
        .filter(Log.id == log_id)
        .first()
    )


# ==================================================
# 新增日志
# ==================================================
def create_log(
    db: Session,
    title: str,
    content: str,
    author: str,
    created_at
):
    """
    新增日志

    ORM实际上会生成：

    INSERT INTO logs(...)
    VALUES(...)
    """

    # 创建ORM对象
    log = Log(
        title=title,
        content=content,
        author=author,
        created_at=created_at
    )

    # 添加到Session
    db.add(log)

    # 提交事务
    db.commit()

    # 刷新对象
    # 刷新以后才能获得数据库生成的id
    db.refresh(log)

    return log


# ==================================================
# 更新日志
# ==================================================
def update_log(
    db: Session,
    log_id: int,
    title: str,
    content: str,
    author: str
):
    """
    更新日志

    ORM底层：

    UPDATE logs
    SET ...
    WHERE id=?
    """

    log = get_log_by_id(
        db,
        log_id
    )

    if log is None:
        return None

    # 修改对象属性
    log.title = title
    log.content = content
    log.author = author

    # 提交修改
    db.commit()

    # 重新同步数据库数据
    db.refresh(log)

    return log


# ==================================================
# 删除日志
# ==================================================
def delete_log(
    db: Session,
    log_id: int
):
    """
    删除日志

    ORM底层：

    DELETE FROM logs
    WHERE id=?
    """

    log = get_log_by_id(
        db,
        log_id
    )

    if log is None:
        return None

    db.delete(log)

    db.commit()

    return True


# ==================================================
# 模糊搜索
# ==================================================
def search_logs(
    db: Session,
    keyword: str
):
    """
    标题模糊搜索

    SQL：

    SELECT *
    FROM logs
    WHERE title LIKE '%keyword%'
    """

    return (
        db.query(Log)
        .filter(
            Log.title.like(
                f"%{keyword}%"
            )
        )
        .all()
    )


# ==================================================
# 日志数量
# ==================================================
def get_total_logs(
    db: Session
):
    """
    获取日志总数

    SQL：

    SELECT COUNT(*)
    FROM logs
    """

    return db.query(Log).count()


# ==================================================
# 作者统计
# ==================================================
def get_author_stats(
    db: Session
):
    """
    每个作者发表了多少日志

    SQL：

    SELECT author,
           COUNT(*)
    FROM logs
    GROUP BY author
    """

    from sqlalchemy import func

    return (
        db.query(
            Log.author,
            func.count(Log.id)
        )
        .group_by(Log.author)
        .all()
    )