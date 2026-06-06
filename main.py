from fastapi import FastAPI

import logger_config

from config import APP_NAME, VERSION
from routers.logs import router
from database import init_db

import config

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
