#!/bin/bash

# 启动Redis（如果未启动）
if ! pgrep -x "redis-server" > /dev/null
then
    echo "Starting Redis..."
    redis-server --daemonize yes
fi

# 安装依赖
echo "Installing dependencies..."
pip install -r requirements.txt

# 启动Streamlit应用
echo "Starting Streamlit app..."
streamlit run app.py --server.port 8501 --server.address 0.0.0.0 