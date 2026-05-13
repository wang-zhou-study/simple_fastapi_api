# Simple FastAPI API

一个使用 FastAPI 编写的简单后端 API 项目。

该项目用于学习：

- FastAPI 基础开发
- RESTful API
- 路由与参数处理
- JSON 数据返回
- 文件读写
- GitHub 项目管理

---

# 功能

## 基础接口

- 首页接口
- 用户信息接口
- 路径参数接口
- 查询参数接口

## 日志接口

- 获取全部日志
- 新增日志
- 搜索日志

---

# 技术栈

- Python 3
- FastAPI
- Uvicorn

---

# 项目结构

```text
simple_fastapi_api/
├── main.py
├── logs.txt
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 安装依赖

```bash
pip install -r requirements.txt
```

---

# 启动项目

```bash
uvicorn main:app --reload
```

启动后访问：

```text
http://127.0.0.1:8000
```

---

# API 文档

FastAPI 会自动生成 Swagger 文档：

```text
http://127.0.0.1:8000/docs
```

---

# API 示例

## 首页接口

```http
GET /
```

返回：

```json
{
  "message": "Hello FastAPI"
}
```

---

## 获取用户信息

```http
GET /user
```

返回：

```json
{
  "name": "wangzhou",
  "age": 25
}
```

---

## 获取指定用户

```http
GET /user/1
```

返回：

```json
{
  "user_id": 1
}
```

---

## 搜索接口

```http
GET /search?keyword=python
```

返回：

```json
{
  "keyword": "python"
}
```

---

# 学习目标

该项目用于练习：

- API 开发
- 后端工程基础
- FastAPI 路由设计
- Git 与 GitHub 工作流

---

# 后续计划

- [ ] 添加 POST 接口
- [ ] 使用 Pydantic
- [ ] 添加 logging
- [ ] 添加错误处理
- [ ] 项目模块化拆分