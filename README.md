# 重庆身份坐标 (ChongQing Identity Map)

基于Streamlit和Redis的重庆身份象限实验系统，通过问卷与实时数据可视化，探索"重庆人"身份的多维度特征。

## 项目简介

本项目是一个互动问卷系统，通过与重庆相关的身份、文化、地理、生活习惯等问题，将每位参与者的"重庆人"身份映射到二维坐标系上。

- **三大章节问卷**：基础身份信息、文化地理习惯、代表性游戏
- **身份坐标**：x轴（实际重庆人）和y轴（精神重庆人）
- **实时可视化**：四象限展示参与者的身份定位

## 快速开始

### 使用Docker（推荐）

```bash
# 使用Docker Compose
docker-compose up -d

# 或直接运行容器
docker run -d -p 8501:8501 \
  -e REDIS_HOST=your_redis_host \
  -e REDIS_PORT=6379 \
  -e REDIS_PASSWORD=your_redis_password \
  ghcr.io/odysseusailoon/chongqing-identity-map:latest
```

### 本地开发

```bash
# 复制环境变量配置文件
cp .env.example .env

# 安装依赖
pip install -r requirements.txt

# 启动应用
streamlit run app.py
```

应用将在 http://localhost:8501 启动

## 系统架构

```
├── app.py                 # Streamlit主应用
├── backend/
│   ├── redis_manager.py   # Redis数据管理
│   └── scoring_engine.py  # 评分引擎
├── config/
│   └── questions.py       # 问题配置
└── requirements.txt       # 依赖包
```

## 配置说明

### 环境变量

| 变量名 | 说明 | 默认值 | 示例 |
|--------|------|--------|------|
| `REDIS_HOST` | Redis主机地址 | `localhost` | `redis.example.com` |
| `REDIS_PORT` | Redis端口 | `6379` | `6379` |
| `REDIS_PASSWORD` | Redis密码 | 无 | `your-password` |
| `REDIS_DB` | Redis数据库编号 | `0` | `0` |

## 评分与可视化

- **评分规则**：静态权重、实时排名、距离评分、众数投票、动态Y/N
- **坐标映射**：答案经多维度加权与排名，投射到[-100, 100]的二维象限
- **四象限标签**：实际&精神重庆人、实际&非精神重庆人、非实际&精神重庆人、非实际&非精神重庆人

## 数据存储

所有数据存储在Redis中：
- 用户答案：`user:answers:{user_id}`
- 用户得分：`user:scores:{user_id}`
- 问题统计：`question:stats:{question_id}`
- 排行榜：`leaderboard:users`

## 自动化部署

本项目配置了GitHub Actions工作流，可自动构建并发布Docker镜像。

### 镜像信息
- **Registry**: GitHub Container Registry (ghcr.io)
- **镜像名**: `ghcr.io/odysseusailoon/chongqing-identity-map`
- **标签**: `latest`, `master-<sha>`, `pr-<number>`

### 更新应用
```bash
# 拉取最新镜像
docker pull ghcr.io/odysseusailoon/chongqing-identity-map:latest

# 重启服务
docker-compose down
docker-compose up -d
```

## 故障排除

### 常见问题
1. **容器无法启动**: 检查端口占用、环境变量配置
2. **无法连接Redis**: 确认Redis服务运行、检查网络连接
3. **应用响应缓慢**: 检查系统资源使用情况

### 查看日志
```bash
# 查看容器日志
docker logs chongqing-identity-map

# 实时查看日志
docker logs -f chongqing-identity-map
```

## 致谢

本项目灵感来源于剧场实验《伍零零》，感谢所有参与者与支持者！

---

如有建议或合作意向，欢迎联系项目维护者。