from fastapi import FastAPI

import logger_config
import config
import logging
import time

from config import (
    APP_NAME,
    VERSION,
    DB_NAME
)
from routers.logs import router
from database import init_db
from fastapi import Request
from fastapi import Request
from fastapi.responses import JSONResponse
from exceptions.custom_exception import LogNotFoundException

from exceptions.handlers import log_not_found_handler


print(DB_NAME)
print(config.__file__)

app = FastAPI(    
    title=APP_NAME,
    version=VERSION)

init_db()

app.include_router(router)


@app.get("/")
def home():

    return {
        "message": "Hello FastAPI"
    }


@app.middleware("http")
async def log_requests(
    request: Request,
    call_next
):

    start_time = time.time()

    logging.info(
        f"开始请求: {request.method} {request.url}"
    )

    response = await call_next(request)

    process_time = time.time() - start_time

    logging.info(
        f"请求结束: {process_time:.4f}秒"
    )

    return response

@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception
):

    return JSONResponse(
        status_code=500,
        content={
            "code": 500,
            "message": str(exc),
            "data": None
        }
    )

@app.middleware("http")
async def log_requests(
    request: Request,
    call_next
):

    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    response.headers[
        "X-Process-Time"
    ] = str(round(process_time, 4))

    return response

app.add_exception_handler(
    LogNotFoundException,
    log_not_found_handler
)