# 重庆身份坐标 Docker 部署指南

本文档提供了使用 Docker 部署重庆身份坐标问卷系统的说明。

## 前提条件

- 已安装 Docker 和 Docker Compose
- 已有一个运行中的 Redis 容器，名称为 `redis_service`，端口为 6379

## 部署步骤

### 1. 设置环境变量

如果您的 Redis 服务有密码保护，请设置环境变量：

```bash
# 设置 Redis 密码环境变量
export PANEL_REDIS_ROOT_PASSWORD=your_redis_password
```

如果没有密码，可以跳过此步骤。

### 2. 构建并启动应用

```bash
# 在项目根目录下执行
cd questionnaire_system
docker-compose up -d
```

### 3. 访问应用

应用将在以下地址运行：

```
http://localhost:8501
```

## 配置说明

### 环境变量

应用容器使用以下环境变量连接到 Redis：

- `REDIS_HOST`: Redis 服务器主机名（默认为 `redis_service`）
- `REDIS_PORT`: Redis 服务器端口（默认为 `6379`）
- `REDIS_PASSWORD`: Redis 服务器密码（如果有）

您可以在 docker-compose.yml 中修改这些环境变量，或者通过环境变量传递：

```bash
REDIS_HOST=custom_host REDIS_PORT=6380 docker-compose up -d
```

## 故障排除

### 无法连接到 Redis

如果应用无法连接到 Redis，请检查：

1. Redis 容器是否正在运行：`docker ps | grep redis_service`
2. Redis 端口是否正确暴露：`docker port redis_service`
3. 环境变量是否正确设置：检查 docker-compose.yml 中的环境变量配置
4. 如果 Redis 有密码保护，确保 `PANEL_REDIS_ROOT_PASSWORD` 环境变量已正确设置

### 应用无法启动

如果应用容器无法启动，请检查日志：

```bash
docker logs questionnaire_system_app_1
```