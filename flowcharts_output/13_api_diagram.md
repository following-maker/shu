# 核心API接口设计

```mermaid
mindmap
  root((API接口))
    认证授权 /api/auth
      POST /register
      POST /login
      POST /logout
      GET /info
      PUT /password
    用户管理 /api/admin/users
      GET /list
      PUT /status
      PUT /role
      DELETE /{id}
    文章管理 /api/articles
      GET /list "分页/筛选"
      GET /{id} "详情"
      POST /create
      PUT /{id}
      DELETE /{id}
      PUT /{id}/top
      PUT /{id}/status
    分类管理 /api/categories
      GET /list
      POST /create
      PUT /{id}
      DELETE /{id}
    标签管理 /api/tags
      GET /list
      POST /create
      PUT /{id}
      DELETE /{id}
    评论管理 /api/comments
      GET /list "按文章/状态"
      POST /create
      PUT /{id}/audit
      DELETE /{id}
    搜索 /api/search
      GET /articles "关键词搜索"
```
