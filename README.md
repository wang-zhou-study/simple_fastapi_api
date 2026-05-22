# Simple FastAPI API

一个基于 FastAPI + SQLite 构建的简易日志管理 API 项目。

该项目用于学习：

- FastAPI 接口开发
- RESTful API 设计
- SQLite 数据库操作
- Pydantic 数据校验
- logging 日志记录
- Python 工程化项目结构

---

# 项目功能

## 日志功能

- 新增日志
- 获取全部日志
- 获取单条日志
- 错误处理（404）
- logging 日志记录

---

# 技术栈

- Python 3
- FastAPI
- Uvicorn
- SQLite
- Pydantic

---

# 项目结构

```text
simple_api/
│
├── models/
│   ├── __init__.py
│   └── log_model.py
│
├── routers/
│   ├── __init__.py
│   └── logs.py
│
├── utils/
│   ├── __init__.py
│   └── file_handler.py
│
├── database.py
├── logger_config.py
├── main.py
├── requirements.txt
├── README.md
└── logs.db
```

---

# API 接口

## 获取全部日志

```http
GET /logs
```

---

## 新增日志

```http
POST /logs
```

请求示例：

```json
{
  "title": "学习 FastAPI",
  "content": "今天学习了 POST 接口",
  "author": "wangzhou"
}
```

---

## 获取单条日志

```http
GET /logs/{log_id}
```

---

# 错误处理

当日志不存在时：

```json
{
  "detail": "日志不存在"
}
```

状态码：

```http
404 Not Found
```

---

# logging 日志系统

项目使用 Python logging 模块记录 API 操作日志。

日志文件：

```text
app.log
```

日志示例：

```text
2026-05-12 20:10:21 - INFO - 获取全部日志
```

---

# 本地运行

## 1. 克隆项目

```bash
git clone git@github.com:wang-zhou-study/simple_fastapi_api.git
```

---

## 2. 安装依赖

```bash
pip install -r requirements.txt
```

---

## 3. 启动项目

```bash
uvicorn main:app --reload
```

---

# Swagger API 文档

启动后访问：

```text
http://127.0.0.1:8000/docs
```

---

# 学习目标

该项目主要用于练习：

- FastAPI 基础开发
- RESTful API
- 数据库操作
- Python 工程化
- 后端开发基础

后续计划：

- 更新日志接口
- 删除日志接口
- 用户登录系统
- JWT 鉴权
- SQLAlchemy ORM
- Docker 部署

---

# 作者

GitHub:

https://github.com/wang-zhou-study

