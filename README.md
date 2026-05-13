# Simple FastAPI API

一个用于学习 FastAPI 的简单后端项目。

## 功能

- Hello API
- 用户接口
- 路径参数
- 查询参数

## 启动方式

```bash
uvicorn main:app --reload
```

## 接口示例

### 首页

```text
GET /
```

### 获取用户

```text
GET /user
```

### 获取指定用户

```text
GET /user/1
```

### 搜索

```text
GET /search?keyword=python
```