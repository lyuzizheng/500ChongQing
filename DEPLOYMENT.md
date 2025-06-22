# 部署指南

本文档介绍如何使用 GitHub Actions 自动构建的 Docker 镜像部署重庆身份坐标问卷系统。

## 🚀 快速部署

### 前提条件
- Docker 和 Docker Compose 已安装
- Redis 服务器（可选，可使用 Docker 运行）

### 方式一：使用 Docker Compose（推荐）

1. **下载配置文件**
```bash
# 创建项目目录
mkdir chongqing-identity-map && cd chongqing-identity-map

# 下载 docker-compose.yml
curl -O https://raw.githubusercontent.com/[username]/ChongQingIdentityMap-/master/questionnaire_system/docker-compose.yml
```

2. **修改配置**
编辑 `docker-compose.yml`，将构建配置改为使用预构建镜像：
```yaml
version: '3'

services:
  app:
    image: ghcr.io/[username]/chongqingidentitymap-:latest
    ports:
      - "8501:8501"
    environment:
      - REDIS_HOST=redis_service
      - REDIS_PORT=6379
      - REDIS_PASSWORD=secure_password_123
    restart: always
    depends_on:
      - redis

  redis:
    image: redis:7-alpine
    command: redis-server --requirepass secure_password_123
    restart: always
    volumes:
      - redis_data:/data

volumes:
  redis_data:
```

3. **启动服务**
```bash
docker-compose up -d
```

4. **访问应用**
打开浏览器访问：http://localhost:8501

### 方式二：单独运行容器

1. **启动 Redis**
```bash
docker run -d --name redis \
  -p 6379:6379 \
  redis:7-alpine redis-server --requirepass your_password
```

2. **启动应用**
```bash
docker run -d --name chongqing-identity-map \
  -p 8501:8501 \
  -e REDIS_HOST=localhost \
  -e REDIS_PORT=6379 \
  -e REDIS_PASSWORD=your_password \
  --link redis:redis_service \
  ghcr.io/[username]/chongqingidentitymap-:latest
```

## 🔧 配置选项

### 环境变量

| 变量名 | 默认值 | 说明 |
|--------|--------|------|
| `REDIS_HOST` | `redis_service` | Redis 服务器地址 |
| `REDIS_PORT` | `6379` | Redis 端口 |
| `REDIS_PASSWORD` | - | Redis 密码（可选） |
| `PYTHONUNBUFFERED` | `1` | Python 输出缓冲控制 |
| `PYTHONDONTWRITEBYTECODE` | `1` | 禁止生成 .pyc 文件 |

### 端口映射
- 容器内端口：`8501`
- 建议主机端口：`8501`

## 🌐 生产环境部署

### 使用反向代理（Nginx）

1. **Nginx 配置示例**
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

2. **HTTPS 配置（使用 Let's Encrypt）**
```bash
# 安装 certbot
sudo apt install certbot python3-certbot-nginx

# 获取 SSL 证书
sudo certbot --nginx -d your-domain.com
```

### 使用 Docker Swarm

1. **创建 stack 文件**
```yaml
# docker-stack.yml
version: '3.8'

services:
  app:
    image: ghcr.io/[username]/chongqingidentitymap-:latest
    ports:
      - "8501:8501"
    environment:
      - REDIS_HOST=redis
      - REDIS_PORT=6379
      - REDIS_PASSWORD_FILE=/run/secrets/redis_password
    secrets:
      - redis_password
    deploy:
      replicas: 2
      restart_policy:
        condition: on-failure
    depends_on:
      - redis

  redis:
    image: redis:7-alpine
    command: redis-server --requirepass-file /run/secrets/redis_password
    secrets:
      - redis_password
    volumes:
      - redis_data:/data
    deploy:
      replicas: 1
      restart_policy:
        condition: on-failure

secrets:
  redis_password:
    external: true

volumes:
  redis_data:
```

2. **部署 stack**
```bash
# 创建密钥
echo "your_secure_password" | docker secret create redis_password -

# 部署 stack
docker stack deploy -c docker-stack.yml chongqing-app
```

## 📊 监控和日志

### 查看日志
```bash
# Docker Compose
docker-compose logs -f app

# 单独容器
docker logs -f chongqing-identity-map
```

### 健康检查
```bash
# 检查容器状态
docker ps

# 检查健康状态
docker inspect --format='{{.State.Health.Status}}' chongqing-identity-map

# 手动健康检查
curl -f http://localhost:8501/_stcore/health
```

### 性能监控
```bash
# 查看资源使用情况
docker stats chongqing-identity-map

# 查看容器详细信息
docker inspect chongqing-identity-map
```

## 🔄 更新和维护

### 更新应用
```bash
# 拉取最新镜像
docker pull ghcr.io/[username]/chongqingidentitymap-:latest

# 重启服务（Docker Compose）
docker-compose down
docker-compose up -d

# 重启服务（单独容器）
docker stop chongqing-identity-map
docker rm chongqing-identity-map
# 然后重新运行容器
```

### 数据备份
```bash
# 备份 Redis 数据
docker exec redis redis-cli --rdb /data/backup.rdb

# 复制备份文件
docker cp redis:/data/backup.rdb ./redis-backup-$(date +%Y%m%d).rdb
```

### 数据恢复
```bash
# 停止服务
docker-compose down

# 恢复数据
docker cp ./redis-backup-20231201.rdb redis:/data/dump.rdb

# 重启服务
docker-compose up -d
```

## 🛠️ 故障排除

### 常见问题

1. **容器无法启动**
   - 检查端口是否被占用
   - 验证环境变量配置
   - 查看容器日志

2. **无法连接 Redis**
   - 确认 Redis 服务正在运行
   - 检查网络连接
   - 验证密码配置

3. **应用响应缓慢**
   - 检查系统资源使用情况
   - 增加容器资源限制
   - 考虑使用多个副本

### 调试命令
```bash
# 进入容器调试
docker exec -it chongqing-identity-map /bin/bash

# 检查网络连接
docker network ls
docker network inspect bridge

# 查看容器资源使用
docker stats --no-stream
```

## 📞 支持

如果遇到问题，请：
1. 查看 [GitHub Issues](https://github.com/[username]/ChongQingIdentityMap-/issues)
2. 提交新的 Issue 并附上详细的错误信息和日志
3. 参考项目文档和 README

---

**注意**: 请将文档中的 `[username]` 替换为实际的 GitHub 用户名或组织名。