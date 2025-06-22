FROM python:3.9-slim

# Build arguments
ARG BUILDTIME
ARG VERSION

# Labels for better image metadata
LABEL org.opencontainers.image.title="ChongQing Identity Map" \
      org.opencontainers.image.description="重庆身份坐标问卷系统" \
      org.opencontainers.image.created="${BUILDTIME}" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.source="https://github.com/username/ChongQingIdentityMap-"

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user for security
RUN groupadd -r appuser && useradd -r -g appuser appuser && \
    mkdir -p /app/.cache && \
    chown -R appuser:appuser /app

# Copy requirements file
COPY --chown=appuser:appuser requirements.txt .

# Switch to non-root user
USER appuser

# Install dependencies as non-root user
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --user -r requirements.txt

# Copy application code
COPY --chown=appuser:appuser . .

# Expose Streamlit port
EXPOSE 8501

# Set environment variables for Redis connection and Python
# These can be overridden by docker-compose or docker run command
ENV REDIS_HOST=redis_service \
    REDIS_PORT=6379 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH=/app/.local/bin:$PATH \
    PYTHONPATH=/app

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1

# Command to run the application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true", "--server.fileWatcherType=none"]