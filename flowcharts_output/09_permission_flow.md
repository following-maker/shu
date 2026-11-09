# 权限控制流程

```mermaid
flowchart TD
    A[前端发起请求] --> B[携带JWT Token]
    B --> C[后端拦截器拦截]
    C --> D{Token有效性}
    D -->|无效/过期| E[返回401未授权]
    E --> F[前端清除Token跳转登录]
    D -->|有效| G[解析用户ID/角色]
    G --> H{权限校验}
    H -->|注解@PreAuthorize| I[检查角色权限]
    H -->|URL拦截| J[检查路径权限]
    I -->|通过| K[放行执行业务]
    J -->|通过| K
    I -->|拒绝| L[返回403禁止访问]
    J -->|拒绝| L
    L --> M[前端提示无权限]
    
    subgraph 角色权限矩阵
        N[普通用户] --> N1[文章增删改查-自己的]
        N --> N2[评论提交]
        N --> N3[个人信息修改]
        O[管理员] --> O1[用户管理]
        O --> O2[所有文章管理]
        O --> O3[分类标签管理]
        O --> O4[评论审核]
        O --> O5[系统设置]
    end
    
    style A fill:#e1f5fe
    style K fill:#c8e6c9
    style F fill:#ffcdd2
    style M fill:#ffcdd2
```
