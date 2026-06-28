# 📘 Simple Log API

一个使用 **FastAPI + SQLite** 编写的日志管理系统。

这是我的 Python 后端学习项目，目前主要用于学习 RESTful API、项目分层、数据库操作以及 FastAPI 开发。

---

# 项目功能

目前已经完成：

- ✅ 新增日志
- ✅ 查询全部日志
- ✅ 根据 ID 查询日志
- ✅ 修改日志
- ✅ 删除日志
- ✅ 标题搜索
- ✅ 分页查询
- ✅ 请求日志记录
- ✅ 作者统计
- ✅ 全部日志数量统计
- ✅ Service 层重构
- ✅ 统一响应格式
- ✅ 自定义异常

---

# 技术栈

- Python 3.14
- FastAPI
- SQLite3
- Uvicorn
- Pydantic
- Logging

---

# 项目结构

```
simple_api
│
├── main.py                 # FastAPI入口
├── config.py               # 项目配置
├── database.py             # 初始化数据库
├── database_manager.py     # 数据库连接管理
├── logger_config.py        # 日志配置
│
├── models
│     └── log_model.py
│
├── routers
│     └── logs.py
│
├── services
│     └── log_services.py
│
├── utils
│     ├── response.py
│     ├── pagination.py
│     └── file_handler.py
│
├── exceptions
│     └── custom_exception.py
│
└── logs.db
```

---

# 项目分层

```
HTTP请求
      │
      ▼
routers
      │
      ▼
services
      │
      ▼
SQLite
      │
      ▼
返回数据
      │
      ▼
统一Response
```

这样每一层只负责自己的工作：

Router

- 接收请求
- 参数校验
- 返回响应

Service

- 操作数据库
- SQL 编写
- 返回数据

Utils

- 工具函数
- 分页
- Response
- 日志

Models

- 数据模型
- 请求参数验证

Exceptions

- 自定义异常

---

# API

## 获取所有日志

GET

```
/logs?page=1&size=5
```

---

## 获取单条日志

GET

```
/logs/{id}
```

---

## 新增日志

POST

```
/logs
```

Body

```json
{
    "title":"Python",
    "content":"FastAPI学习",
    "author":"zhou"
}
```

---

## 修改日志

PUT

```
/logs/{id}
```

---

## 删除日志

DELETE

```
/logs/{id}
```

---

## 搜索日志

GET

```
/search?keyword=Python
```

---

## 作者统计

GET

```
/stats/authors
```

---

## 日志总数

GET

```
/stats
```

---

# 返回格式

成功：

```json
{
    "code":200,
    "message":"success",
    "data":[]
}
```

失败：

```json
{
    "code":400,
    "message":"error",
    "data":null
}
```

---

# 已完成学习内容

✔ FastAPI 路由

✔ RESTful API

✔ SQLite 数据库

✔ SQL 基础

✔ CRUD

✔ Pydantic

✔ Service 分层

✔ Logging

✔ 分页查询

✔ 查询参数

✔ 自定义异常

✔ 统一返回格式

---

# 下一步计划

准备继续学习：

- [ ] 数据库连接池
- [ ] SQLAlchemy ORM
- [ ] Repository 模式
- [ ] JWT 登录认证
- [ ] 用户系统
- [ ] Token 权限
- [ ] 文件上传
- [ ] Docker 部署
- [ ] Pytest 自动化测试

---

# 学习目标

通过这个项目逐步学习：

- Python 后端开发
- FastAPI
- RESTful API
- 数据库设计
- Web 开发
- 项目架构设计

最终完成一个具有完整登录、权限、数据库、部署能力的小型后端项目。

---

## 作者

GitHub：

https://github.com/wang-zhou-study

学习方向：

* Python 后端开发
* FastAPI
* 数据库开发
* 工程化项目实践
