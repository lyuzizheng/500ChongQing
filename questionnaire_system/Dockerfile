FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Set environment variables for Redis connection
# These can be overridden by docker-compose or docker run command
ENV REDIS_HOST=redis_service
ENV REDIS_PORT=6379
# REDIS_PASSWORD will be provided by docker-compose

# Command to run the application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]