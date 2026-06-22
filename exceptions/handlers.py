from fastapi import Request
from fastapi.responses import JSONResponse

from exceptions.custom_exception import (
    LogNotFoundException
)


async def log_not_found_handler(
    request: Request,
    exc: LogNotFoundException
):

    return JSONResponse(
        status_code=404,
        content={
            "code":404,
            "message":exc.message,
            "data":None
        }
    )