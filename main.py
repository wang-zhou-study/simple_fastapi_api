from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

LOG_FILE = "logs.txt"

#数据模型
class LogItem(BaseModel):
    title: str
    content: str
    author: str

@app.get("/")
def home():
    return {"message":"hello fastapi"}

#获取全部日志
@app.get("/logs")
def get_logs():

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            logs = f.readlines()

        logs = [log.strip() for log in logs]

        return{
            "logs":logs
        }
    
    except FileNotFoundError:
        return{
            "error":"日志不存在"
        }

# 新增日志
@app.post("/logs")
def add_log(log: LogItem):

    log_text = (
        f"标题: {log.title} | "
        f"内容: {log.content} | "
        f"作者: {log.author}"
    )

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_text + "\n")

    return {
        "message": "日志添加成功",
        "log": log
    }

# 搜索日志
@app.get("/logs/search")
def search_logs(keyword: str):

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            logs = f.readlines()

        result = []

        for log in logs:
            if keyword.lower() in log.lower():
                result.append(log.strip())

        return {
            "keyword": keyword,
            "result": result
        }

    except FileNotFoundError:
        return {
            "error": "日志文件不存在"
        }

