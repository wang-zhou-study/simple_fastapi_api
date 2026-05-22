from fastapi import FastAPI

import logger_config

from routers.logs import router
from database import init_db

app = FastAPI()

init_db()

app.include_router(router)


@app.get("/")
def home():

    return {
        "message": "Hello FastAPI"
    }
