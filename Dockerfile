# 使用 Ubuntu 基础镜像
FROM ubuntu:20.04

# 设置环境变量避免交互式提示
ENV DEBIAN_FRONTEND=noninteractive

# 安装必要的包
RUN apt-get update && apt-get install -y \
  wget \
  software-properties-common \
  python3.9 \
  python3-pip \
  wine64 \
  xvfb \
  && rm -rf /var/lib/apt/lists/*

# 设置 Wine 环境
ENV WINEARCH=win64
ENV WINEPREFIX=/root/.wine
RUN wine64 wineboot --init

# 安装 Windows 版本的 Python
RUN wget https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe && \
  xvfb-run wine64 python-3.9.0-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 && \
  rm python-3.9.0-amd64.exe

# 设置 Wine Python 路径
ENV WINE_PYTHON="wine64 C:\\\\users\\\\root\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python39\\\\python.exe"

# 复制项目文件
COPY . /app
WORKDIR /app

# 使用 Wine Python 安装依赖和 PyInstaller
RUN ${WINE_PYTHON} -m pip install -r requirements.txt
RUN ${WINE_PYTHON} -m pip install pyinstaller

# 使用 Wine Python 运行 PyInstaller
RUN ${WINE_PYTHON} -m PyInstaller build_config.spec