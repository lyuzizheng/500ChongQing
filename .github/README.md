# GitHub Actions 自动化部署

本项目配置了 GitHub Actions 工作流，可以在推送到 `master` 或 `main` 分支时自动构建并发布 Docker 镜像。

## 🚀 自动化流程

### 触发条件
- 推送到 `master` 或 `main` 分支
- 创建针对 `master` 或 `main` 分支的 Pull Request

### 构建特性
- ✅ 多平台构建 (linux/amd64, linux/arm64)
- ✅ 自动缓存优化
- ✅ 镜像测试验证
- ✅ 自动标签管理
- ✅ 部署信息生成

## 📦 镜像信息

### 镜像仓库
- **Registry**: GitHub Container Registry (ghcr.io)
- **镜像名**: `ghcr.io/[username]/chongqingidentitymap-`
- **标签策略**:
  - `latest`: 最新的 master/main 分支构建
  - `master-<sha>`: 基于 commit SHA 的标签
  - `pr-<number>`: Pull Request 构建标签

### 使用镜像

#### 1. 拉取最新镜像
```bash
docker pull ghcr.io/[username]/chongqingidentitymap-:latest
```

#### 2. 运行容器
```bash
docker run -d -p 8501:8501 \
  -e REDIS_HOST=your_redis_host \
  -e REDIS_PORT=6379 \
  -e REDIS_PASSWORD=your_redis_password \
  --name chongqing-identity-map \
  ghcr.io/[username]/chongqingidentitymap-:latest
```

#### 3. 使用 Docker Compose
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
      - REDIS_PASSWORD=your_password
    restart: always

  redis:
    image: redis:7-alpine
    command: redis-server --requirepass your_password
    restart: always
```

## 🔧 配置说明

### 环境变量
- `REDIS_HOST`: Redis 服务器地址
- `REDIS_PORT`: Redis 端口 (默认: 6379)
- `REDIS_PASSWORD`: Redis 密码

### 权限要求
GitHub Actions 需要以下权限：
- `contents: read` - 读取仓库内容
- `packages: write` - 推送到 GitHub Container Registry

## 📋 工作流详情

### 构建步骤
1. **检出代码** - 获取最新代码
2. **设置 Docker Buildx** - 启用多平台构建
3. **登录容器注册表** - 使用 GITHUB_TOKEN 认证
4. **提取元数据** - 生成标签和标签
5. **构建和推送** - 多平台构建并推送镜像
6. **生成部署信息** - 在 Actions 摘要中显示使用说明
7. **测试镜像** - 验证构建的镜像可以正常启动

### 缓存优化
- 使用 GitHub Actions 缓存 (GHA)
- 自动缓存 Docker 层以加速后续构建

## 🛠️ 本地开发

### 本地构建镜像
```bash
cd questionnaire_system
docker build -t chongqing-identity-map .
```

### 本地运行
```bash
docker run -d -p 8501:8501 \
  -e REDIS_HOST=localhost \
  -e REDIS_PORT=6379 \
  chongqing-identity-map
```

## 🔍 故障排除

### 常见问题
1. **权限错误**: 确保仓库启用了 GitHub Container Registry
2. **构建失败**: 检查 Dockerfile 和依赖项
3. **镜像无法启动**: 验证环境变量配置

### 查看日志
```bash
# 查看容器日志
docker logs chongqing-identity-map

# 实时查看日志
docker logs -f chongqing-identity-map
```

## 📚 相关文档
- [GitHub Actions 文档](https://docs.github.com/en/actions)
- [GitHub Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)
- [Docker 多平台构建](https://docs.docker.com/build/building/multi-platform/)