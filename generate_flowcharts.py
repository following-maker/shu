#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
毕业设计流程图生成脚本
基于Spring Boot + Vue个人博客系统开题报告生成Mermaid流程图
可导出为Markdown、HTML、PNG、SVG等格式
"""

import os
from pathlib import Path


class FlowchartGenerator:
    """流程图生成器"""
    
    def __init__(self, output_dir: str = "output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def get_architecture_diagram(self) -> str:
        """系统总体架构图 - 树状结构"""
        return '''graph TD
    Root((个人博客系统)) --> Frontend["🖥️ 前端层"]
    Root --> Gateway["🌐 网关层"]
    Root --> Backend["⚙️ 后端层"]
    Root --> Data["💾 数据层"]
    Root --> Infra["📦 基础设施"]
    
    Frontend --> FE1["Vue 3 前端应用"]
    FE1 --> FE1a["用户端页面"]
    FE1 --> FE1b["管理端页面"]
    FE1 --> FE1c["Axios 请求库"]
    FE1 --> FE1d["Pinia 状态管理"]
    FE1 --> FE1e["Vue Router 路由"]
    
    Gateway --> GW1["Nginx 反向代理"]
    GW1 --> GW1a["静态资源服务"]
    GW1 --> GW1b["API 转发"]
    GW1 --> GW1c["跨域处理"]
    
    Backend --> BE1["Spring Boot 3.x 应用"]
    BE1 --> BE1a["Controller 控制层"]
    BE1 --> BE1b["Service 业务层"]
    BE1 --> BE1c["Mapper 数据访问层"]
    BE1 --> BE1d["Security 权限控制"]
    BE1 --> BE1e["JWT 认证授权"]
    
    Data --> DB1["MySQL 8.0 数据库"]
    DB1 --> DB1a["用户表"]
    DB1 --> DB1b["文章表"]
    DB1 --> DB1c["分类表"]
    DB1 --> DB1d["标签表"]
    DB1 --> DB1e["评论表"]
    DB1 --> DB1f["文章标签关联表"]
    
    Infra --> INF1["Redis 缓存"]
    Infra --> INF2["文件存储"]
    
    style Root fill:#1565c0,color:#fff
    style Frontend fill:#42b883,color:#fff
    style Gateway fill:#0096d6,color:#fff
    style Backend fill:#6db33f,color:#fff
    style Data fill:#f29111,color:#fff
    style Infra fill:#9c27b0,color:#fff'''

    def get_modules_diagram(self) -> str:
        """系统功能模块图"""
        return '''mindmap
  root((个人博客系统))
    用户端
      用户认证
        注册
        登录/JWT
        登出
      博客展示
        首页/文章列表
        文章详情
        分类浏览
        标签浏览
        文章搜索
      交互功能
        评论提交
        评论展示
      个人中心
        个人信息
        我的文章
        修改密码
    管理端
      管理员认证
        登录/JWT
      用户管理
        用户列表
        启用/禁用
        角色分配
      文章管理
        文章列表
        发布/编辑
        审核/删除
        置顶设置
      分类管理
        分类增删改查
        排序
      标签管理
        标签增删改查
      评论管理
        评论列表
        审核通过/拒绝
        删除
      系统设置
        站点配置
        友链管理'''

    def get_auth_flow(self) -> str:
        """用户注册登录流程"""
        return '''flowchart TD
    A[用户访问注册/登录页] --> B{选择操作}
    B -->|注册| C[填写用户名/邮箱/密码]
    C --> D[前端表单验证]
    D -->|验证通过| E[发送注册请求]
    E --> F[后端校验用户名/邮箱唯一性]
    F -->|唯一| G[密码加密存储]
    G --> H[返回注册成功]
    H --> I[跳转登录页]
    F -->|已存在| J[返回错误信息]
    J --> C
    
    B -->|登录| K[填写用户名/密码]
    K --> L[前端表单验证]
    L -->|验证通过| M[发送登录请求]
    M --> N[后端校验用户名密码]
    N -->|正确| O[生成JWT Token]
    O --> P[返回Token及用户信息]
    P --> Q[前端存储Token]
    Q --> R[跳转首页/个人中心]
    N -->|错误| S[返回错误信息]
    S --> K
    
    style A fill:#e1f5fe
    style R fill:#c8e6c9
    style I fill:#c8e6c9'''

    def get_article_flow(self) -> str:
        """文章发布管理流程"""
        return '''flowchart TD
    A[用户进入发布文章页] --> B[填写标题/内容/分类/标签]
    B --> C[选择封面图可选]
    C --> D[点击发布/保存草稿]
    D --> E{操作类型}
    E -->|发布| F[状态=已发布]
    E -->|保存草稿| G[状态=草稿]
    F --> H[前端验证必填字段]
    G --> H
    H -->|验证通过| I[发送保存请求]
    I --> J[后端事务处理]
    J --> K[保存文章主表]
    K --> L[处理分类关联]
    L --> M[处理标签关联]
    M --> N[处理标签新建/复用]
    N --> O[返回文章ID]
    O --> P[前端跳转文章详情/列表]
    
    Q[管理员文章审核] --> R[查看待审核列表]
    R --> S{审核操作}
    S -->|通过| T[状态=已发布]
    S -->|拒绝| U[状态=已拒绝+原因]
    S -->|删除| V[逻辑删除]
    T --> W[通知作者]
    U --> W
    
    style A fill:#e1f5fe
    style P fill:#c8e6c9
    style W fill:#c8e6c9'''

    def get_browse_flow(self) -> str:
        """文章浏览搜索流程"""
        return '''flowchart TD
    A[用户访问博客首页] --> B[请求文章列表API]
    B --> C[后端分页查询]
    C --> D[返回文章列表数据]
    D --> E[前端渲染列表]
    E --> F{用户操作}
    
    F -->|点击文章| G[请求文章详情]
    G --> H[后端查询文章+分类+标签+作者]
    H --> I[阅读数+1]
    I --> J[返回详情数据]
    J --> K[前端渲染详情页]
    K --> L[加载评论列表]
    
    F -->|点击分类| M[按分类筛选]
    M --> B
    
    F -->|点击标签| N[按标签筛选]
    N --> B
    
    F -->|搜索关键词| O[发送搜索请求]
    O --> P[后端全文/模糊搜索]
    P --> Q[返回搜索结果]
    Q --> E
    
    F -->|分页| R[请求指定页码]
    R --> B
    
    style A fill:#e1f5fe
    style K fill:#fff3e0'''

    def get_comment_flow(self) -> str:
        """评论提交审核流程"""
        return '''flowchart TD
    A[用户阅读文章] --> B[填写评论内容]
    B --> C[点击提交评论]
    C --> D{用户登录状态}
    D -->|未登录| E[跳转登录页]
    E --> B
    D -->|已登录| F[发送评论请求]
    F --> G[后端保存评论]
    G --> H[状态=待审核]
    H --> I[返回提交成功]
    I --> J[前端提示待审核]
    
    K[管理员评论管理] --> L[查看评论列表]
    L --> M{筛选条件}
    M -->|待审核| N[显示待审核列表]
    M -->|已通过| O[显示已通过列表]
    M -->|已拒绝| P[显示已拒绝列表]
    
    N --> Q{审核操作}
    Q -->|通过| R[状态=已通过]
    Q -->|拒绝| S[状态=已拒绝]
    Q -->|删除| T[逻辑删除]
    R --> U[前端实时更新]
    S --> U
    T --> U
    
    style A fill:#e1f5fe
    style J fill:#fff3e0
    style U fill:#c8e6c9'''

    def get_category_flow(self) -> str:
        """分类标签管理流程"""
        return '''flowchart TD
    subgraph 用户端
        A1[浏览分类列表] --> B1[点击分类查看文章]
        A2[浏览标签云] --> B2[点击标签查看文章]
    end
    
    subgraph 管理端
        C1[分类管理页面] --> D1{操作类型}
        D1 -->|新增| E1[填写分类名/排序/描述]
        D1 -->|编辑| F1[修改分类信息]
        D1 -->|删除| G1[检查关联文章]
        G1 -->|有关联| H1[提示不可删除]
        G1 -->|无关联| I1[执行删除]
        E1 --> J1[保存分类]
        F1 --> J1
        I1 --> J1
        
        C2[标签管理页面] --> D2{操作类型}
        D2 -->|新增| E2[填写标签名]
        D2 -->|编辑| F2[修改标签名]
        D2 -->|删除| G2[检查关联文章]
        G2 -->|有关联| H2[提示不可删除]
        G2 -->|无关联| I2[执行删除]
        E2 --> J2[保存标签]
        F2 --> J2
        I2 --> J2
    end
    
    style A1 fill:#e1f5fe
    style A2 fill:#e1f5fe
    style J1 fill:#c8e6c9
    style J2 fill:#c8e6c9'''

    def get_profile_flow(self) -> str:
        """个人中心管理流程"""
        return '''flowchart TD
    A[用户进入个人中心] --> B[展示用户基本信息]
    B --> C{功能选择}
    
    C -->|我的文章| D[查看文章列表]
    D --> E{文章操作}
    E -->|编辑| F[跳转编辑页]
    E -->|删除| G[确认删除]
    G -->|确认| H[逻辑删除文章]
    E -->|查看| I[跳转详情页]
    
    C -->|修改资料| J[编辑昵称/头像/简介]
    J --> K[保存修改]
    K --> L[更新用户信息]
    
    C -->|修改密码| M[输入旧密码/新密码]
    M --> N[验证旧密码]
    N -->|正确| O[加密新密码保存]
    N -->|错误| P[提示密码错误]
    P --> M
    
    C -->|我的评论| Q[查看评论记录]
    
    style A fill:#e1f5fe
    style L fill:#c8e6c9
    style O fill:#c8e6c9'''

    def get_permission_flow(self) -> str:
        """权限控制流程"""
        return '''flowchart TD
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
    style M fill:#ffcdd2'''

    def get_er_diagram(self) -> str:
        """数据库ER图"""
        return '''erDiagram
    USER ||--o{ ARTICLE : "发布"
    USER ||--o{ COMMENT : "发表"
    ARTICLE ||--o{ COMMENT : "包含"
    CATEGORY ||--o{ ARTICLE : "分类"
    ARTICLE }|--o{ TAG : "标签"
    ARTICLE_TAG }|--o{ TAG : "关联"
    
    USER {
        bigint id PK
        varchar username UK
        varchar password
        varchar email UK
        varchar nickname
        varchar avatar
        varchar bio
        tinyint role "0=用户,1=管理员"
        tinyint status "0=禁用,1=启用"
        datetime create_time
        datetime update_time
    }
    
    ARTICLE {
        bigint id PK
        bigint user_id FK
        bigint category_id FK
        varchar title
        text content
        varchar cover_image
        tinyint status "0=草稿,1=已发布,2=已拒绝"
        tinyint is_top "0=否,1=是"
        int view_count
        datetime create_time
        datetime update_time
        datetime publish_time
    }
    
    CATEGORY {
        bigint id PK
        varchar name
        int sort_order
        varchar description
        tinyint status
        datetime create_time
    }
    
    TAG {
        bigint id PK
        varchar name UK
        int article_count
        datetime create_time
    }
    
    COMMENT {
        bigint id PK
        bigint article_id FK
        bigint user_id FK
        bigint parent_id FK "回复评论"
        text content
        tinyint status "0=待审核,1=已通过,2=已拒绝"
        datetime create_time
    }
    
    ARTICLE_TAG {
        bigint article_id FK
        bigint tag_id FK
    }'''

    def get_deploy_diagram(self) -> str:
        """部署拓扑图"""
        return '''graph TB
    subgraph "用户访问"
        U[用户浏览器]
    end
    
    subgraph "云服务器"
        direction TB
        N[Nginx:80/443]
        N -->|静态资源| S[前端构建产物 dist/]
        N -->|API请求| B[Spring Boot:8080]
        B -->|数据库| DB[(MySQL:3306)]
        B -->|缓存| R[(Redis:6379)]
        B -->|文件| FS[文件存储/对象存储]
    end
    
    U -->|HTTPS| N
    
    subgraph "CI/CD"
        CI[GitHub Actions/GitLab CI]
        CI -->|构建前端| S
        CI -->|构建后端| B
        CI -->|部署| N
    end
    
    style U fill:#e1f5fe
    style N fill:#0096d6,color:#fff
    style B fill:#6db33f,color:#fff
    style DB fill:#f29111,color:#fff'''

    def get_gantt_diagram(self) -> str:
        """甘特图"""
        return '''gantt
    title 毕业设计开发进度安排
    dateFormat  YYYY-MM-DD
    axisFormat  %m-%d
    
    section 阶段一：准备与设计
    需求分析与技术选型     :done, des1, 2026-10-22, 10d
    系统架构设计           :done, des2, 2026-11-01, 5d
    数据库设计             :done, des3, 2026-11-06, 5d
    接口文档设计           :active, des4, 2026-11-11, 5d
    
    section 阶段二：后端开发
    项目搭建与基础配置     :backend1, 2026-11-16, 5d
    用户认证模块           :backend2, 2026-11-21, 7d
    文章管理模块           :backend3, 2026-11-28, 10d
    分类标签模块           :backend4, 2026-12-08, 5d
    评论管理模块           :backend5, 2026-12-13, 5d
    权限控制与通用功能     :backend6, 2026-12-18, 5d
    
    section 阶段三：前端开发
    项目初始化与路由配置   :frontend1, 2026-11-16, 5d
    用户端页面开发         :frontend2, 2026-11-21, 15d
    管理端页面开发         :frontend3, 2026-12-06, 15d
    组件封装与状态管理     :frontend4, 2026-12-21, 7d
    
    section 阶段四：联调测试
    前后端联调             :test1, 2026-12-28, 10d
    功能测试               :test2, 2027-01-07, 10d
    性能测试与优化         :test3, 2027-01-17, 7d
    部署上线               :test4, 2027-01-24, 5d
    
    section 阶段五：论文撰写
    论文初稿撰写           :paper1, 2027-01-01, 30d
    论文修改定稿           :paper2, 2027-03-15, 12d
    答辩准备               :paper3, 2027-03-27, 10d'''

    def get_api_diagram(self) -> str:
        """API接口设计"""
        return '''mindmap
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
      GET /articles "关键词搜索"'''

    def generate_all_markdown(self) -> str:
        """生成完整Markdown文档"""
        diagrams = {
            "1. 系统总体架构图": self.get_architecture_diagram(),
            "2. 系统功能模块图": self.get_modules_diagram(),
            "3. 用户注册登录流程图": self.get_auth_flow(),
            "4. 文章发布与管理流程图": self.get_article_flow(),
            "5. 文章浏览与搜索流程图": self.get_browse_flow(),
            "6. 评论提交与审核流程图": self.get_comment_flow(),
            "7. 分类与标签管理流程图": self.get_category_flow(),
            "8. 个人中心管理流程图": self.get_profile_flow(),
            "9. 权限控制流程图": self.get_permission_flow(),
            "10. 数据库ER图": self.get_er_diagram(),
            "11. 系统部署拓扑图": self.get_deploy_diagram(),
            "12. 开发阶段甘特图": self.get_gantt_diagram(),
            "13. 核心API接口设计": self.get_api_diagram(),
        }
        
        md = "# 毕业设计流程图文档\n\n"
        md += "## 项目概述\n"
        md += "- **项目名称**：基于Spring Boot+Vue的个人博客的设计与实现\n"
        md += "- **技术栈**：Spring Boot 3.x + Vue 3 + MySQL 8.0 + MyBatis-Plus\n"
        md += "- **架构模式**：前后端分离，RESTful API\n"
        md += "- **角色划分**：普通用户（写作者）、管理员\n\n"
        md += "---\n\n"
        
        for title, diagram in diagrams.items():
            md += f"## {title}\n\n"
            md += "```mermaid\n"
            md += diagram
            md += "\n```\n\n"
            md += "---\n\n"
        
        md += "## 📋 技术栈版本建议\n\n"
        md += "| 技术 | 版本 | 说明 |\n"
        md += "|------|------|------|\n"
        md += "| Spring Boot | 3.2.x | JDK 17+ |\n"
        md += "| Vue.js | 3.4.x | Composition API |\n"
        md += "| MySQL | 8.0 | InnoDB引擎 |\n"
        md += "| MyBatis-Plus | 3.5.x | ORM框架 |\n"
        md += "| JWT | jjwt 0.12.x | 认证授权 |\n"
        md += "| Redis | 7.x | 缓存/Session |\n"
        md += "| Nginx | 1.24.x | 反向代理 |\n"
        md += "| Maven | 3.9+ | 后端构建 |\n"
        md += "| Vite | 5.x | 前端构建 |\n\n"
        
        md += "---\n\n"
        md += "*文档生成时间：2026-11-09*\n"
        md += "*基于开题报告《基于Spring Boot+Vue的个人博客的设计与实现》制作*\n"
        
        return md

    def save_markdown(self, filename: str = "graduation_design_flowcharts.md"):
        """保存Markdown文件"""
        content = self.generate_all_markdown()
        filepath = self.output_dir / filename
        filepath.write_text(content, encoding='utf-8')
        print(f"✅ Markdown文件已保存: {filepath}")
        return filepath

    def save_individual_diagrams(self):
        """保存单独的Mermaid文件"""
        diagrams = {
            "01_architecture": ("系统总体架构图", self.get_architecture_diagram()),
            "02_modules": ("系统功能模块图", self.get_modules_diagram()),
            "03_auth_flow": ("用户注册登录流程", self.get_auth_flow()),
            "04_article_flow": ("文章发布管理流程", self.get_article_flow()),
            "05_browse_flow": ("文章浏览搜索流程", self.get_browse_flow()),
            "06_comment_flow": ("评论提交审核流程", self.get_comment_flow()),
            "07_category_flow": ("分类标签管理流程", self.get_category_flow()),
            "08_profile_flow": ("个人中心管理流程", self.get_profile_flow()),
            "09_permission_flow": ("权限控制流程", self.get_permission_flow()),
            "10_er_diagram": ("数据库ER图", self.get_er_diagram()),
            "11_deploy_diagram": ("系统部署拓扑图", self.get_deploy_diagram()),
            "12_gantt_diagram": ("开发进度甘特图", self.get_gantt_diagram()),
            "13_api_diagram": ("核心API接口设计", self.get_api_diagram()),
        }
        
        for filename, (title, diagram) in diagrams.items():
            content = f"# {title}\n\n```mermaid\n{diagram}\n```\n"
            filepath = self.output_dir / f"{filename}.md"
            filepath.write_text(content, encoding='utf-8')
        
        print(f"✅ 单独图表文件已保存至: {self.output_dir}")


def main():
    """主函数"""
    print("=" * 60)
    print("🎓 毕业设计流程图生成器")
    print("   基于Spring Boot + Vue个人博客系统")
    print("=" * 60)
    
    generator = FlowchartGenerator("flowcharts_output")
    
    # 生成完整Markdown文档
    generator.save_markdown()
    
    # 生成单独图表文件
    generator.save_individual_diagrams()
    
    print("\n" + "=" * 60)
    print("✨ 生成完成！")
    print("📁 输出目录: flowcharts_output/")
    print("📄 主文档: graduation_design_flowcharts.md")
    print("📊 单独图表: 13个 .md 文件")
    print("\n💡 使用建议:")
    print("   1. 用VS Code + Markdown Preview Enhanced查看")
    print("   2. 右键导出为PNG/SVG插入Word论文")
    print("   3. 复制Mermaid代码到Notion/Obsidian/GitHub渲染")
    print("=" * 60)


if __name__ == "__main__":
    main()