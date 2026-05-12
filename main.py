from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}

@app.get("/user")
def get_user():
    return {
        "name": "wangzhou",
        "age": 25
    }