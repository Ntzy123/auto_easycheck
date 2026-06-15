#!/bin/bash

# 检查pip最新版本
read -p "是否更换pip清华源？(y/n，默认n): " choice
if [[ "$choice" == "y" || "$choice" == "Y" ]]; then
    python -m pip install --upgrade pip
    pip config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
fi

# 创建虚拟环境
if [ ! -d "venv" ]; then
    echo "正在创建虚拟环境"
    python -m venv venv
    echo "venv环境创建成功！"
    sleep 2
fi

# 激活虚拟环境并安装依赖包
source venv/bin/activate
echo "正在检查并安装依赖包"
python -m pip install --upgrade pip
pip install -r requirements.txt

# 选择打包或退出
clear
echo "============================"
echo "1. 打包为可执行文件"
echo "2. 退出"
echo "============================"
read -n 1 -p "请选择 [1 or 2]: " op
echo

if [ "$op" == "2" ]; then
    exit 0
fi

# 打包
t=$(date +%Y%m%d%H%M%S)
pyinstaller --onefile --name=auto_easycheck run.py
echo "打包完成"
read -n 1 -s -r -p "按任意键继续..."
echo
exit 0
