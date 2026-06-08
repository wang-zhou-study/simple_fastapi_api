# Simple FastAPI Log API

一个基于 FastAPI 开发的日志管理系统练手项目。

## 项目简介

本项目用于学习 FastAPI 后端开发。

目前已实现：

* 创建日志
* 查询日志
* 修改日志
* 删除日志
* 关键词搜索
* 分页查询
* SQLite 数据库存储
* Pydantic 数据校验
* Logging 日志记录

---

## 技术栈

* Python 3.13
* FastAPI
* SQLite3
* Pydantic
* Uvicorn

---

## 项目结构

```text
simple_api/

├── main.py
├── config.py
├── database.py
├── logger_config.py
├── logs.db

├── models/
│   └── log_model.py

├── routers/
│   └── logs.py

├── utils/
│   └── file_handler.py

├── README.md
└── requirements.txt
```

---

## 数据库结构

### logs 表

| 字段         | 类型      |
| ---------- | ------- |
| id         | INTEGER |
| title      | TEXT    |
| content    | TEXT    |
| author     | TEXT    |
| created_at | TEXT    |

---

## API 接口

### 新增日志

**POST**

```http
/logs
```

请求体：

```json
{
  "title": "学习FastAPI",
  "content": "今天学习了数据库",
  "author": "wangzhou"
}
```

返回：

```json
{
  "message": "日志添加成功"
}
```

---

### 获取全部日志

**GET**

```http
/logs
```

---

### 分页查询

**GET**

```http
/logs?page=1&size=5
```

---

### 搜索日志

**GET**

```http
/search?keyword=FastAPI
```

---

### 修改日志

**PUT**

```http
/logs/{id}
```

请求体：

```json
{
  "title": "修改后的标题",
  "content": "修改后的内容",
  "author": "wangzhou"
}
```

---

### 删除日志

**DELETE**

```http
/logs/{id}
```

---

## 启动项目

### 1. 克隆项目

```bash
git clone git@github.com:wang-zhou-study/simple_fastapi_api.git
```

### 2. 进入项目目录

```bash
cd simple_fastapi_api
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 启动项目

```bash
uvicorn main:app --reload
```

---

## 访问接口文档

启动成功后访问：

```text
http://127.0.0.1:8000/docs
```

FastAPI 会自动生成 Swagger API 文档。

---

## 学习收获

通过本项目学习了：

* FastAPI 基础开发
* RESTful API 设计
* APIRouter 路由拆分
* Pydantic 数据模型
* SQLite 数据库操作
* CRUD 实现
* 分页与搜索
* Logging 日志系统
* Git 与 GitHub 协作
* Bug 调试与 Traceback 分析

---

## 已解决的问题

开发过程中解决了以下问题：

* GitHub SSH 配置
* Git Push 网络连接问题
* ImportError 导入错误
* Pydantic 模型定义错误
* SQLite 字段缺失错误
* FastAPI OpenAPI 文档加载失败
* 分页参数未定义错误

---

## 后续计划

* SQLAlchemy ORM
* 用户注册登录
* JWT 身份认证
* Docker 部署
* 自动化测试
* 云服务器部署
* Nginx + Linux 部署

---

## 作者

GitHub：

https://github.com/wang-zhou-study

学习方向：

* Python 后端开发
* FastAPI
* 数据库开发
* 工程化项目实践
