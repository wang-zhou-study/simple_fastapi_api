import logging

from datetime import datetime

from fastapi import APIRouter
from fastapi import HTTPException

from models.log_model import LogItem

from services.log_services import (
    get_all_logs,
    get_log_by_id,
    get_total_logs,
    add_log as add_log_service,
    update_log as update_log_service,
    delete_log as delete_log_service,
    search_logs as search_logs_service
)

from utils.response import (
    success_response,
    error_response
)

router = APIRouter()





@router.post("/logs")
def add_log(log: LogItem):

    logging.info(
        f"新增日志: {log.title}"
    )

    created_at = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    add_log_service(
        log.title,
        log.content,
        log.author,
        created_at
    )

    return success_response(
        message="日志添加成功"
    )


@router.get("/logs")
def get_logs(
    page: int = 1,
    size: int = 5
):

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
def update_log(
    log_id: int,
    log: LogItem
):

    affected = update_log_service(
        log_id,
        log.title,
        log.content,
        log.author
    )

    if affected == 0:

        raise HTTPException(
            status_code=404,
            detail="日志不存在"
        )

    return success_response(
        message="日志更新成功"
    )


@router.delete("/logs/{log_id}")
def delete_log(log_id: int):

    affected = delete_log_service(
        log_id
    )

    if affected == 0:

        raise HTTPException(
            status_code=404,
            detail="日志不存在"
        )

    return success_response(
        message="日志删除成功"
    )


@router.get("/search")
def search_logs(keyword: str):

    logs = search_logs_service(
        keyword
    )

    return success_response(
        data=logs
    )





@router.get("/stats")
def get_stats():

    total = get_total_logs()

    return success_response(
        data={
            "total_logs": total
        }
    )

@router.get("/logs/{log_id}")
def get_log(log_id: int):

    log = get_log_by_id(log_id)

    if log is None:

        raise HTTPException(
            status_code=404,
            detail="日志不存在"
        )

    return success_response(
        data={
            "id": log[0],
            "title": log[1],
            "content": log[2],
            "author": log[3],
            "created_at": log[4]
        }
    )
