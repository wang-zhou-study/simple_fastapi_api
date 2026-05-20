from fastapi import FastAPI
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

