from fastapi import FastAPI

import logger_config
import config
import logging
import time

from config import APP_NAME, VERSION
from routers.logs import router
from database import init_db
from fastapi import Request


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