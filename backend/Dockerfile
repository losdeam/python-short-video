    # 基于镜像基础
    #FROM python:3.9
    FROM python:3.9
    
    

    # 设置工作目录
    WORKDIR /app

    # 复制项目的依赖文件到容器里
    COPY requirements.txt requirements.txt

    # RUN apt-get install ffmpeg libsm6 libxext6  -y

    # # 设置镜像源
    ENV PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple
    ENV PIP_TRUSTED_HOST=pypi.tuna.tsinghua.edu.cn

    # 安装项目依赖
    # RUN pip install opencv-python-headless -i https://pypi.douban.com/simple
    RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ 

    # 复制其他文件到容器里
    COPY . .

    # 设置环境变量
    ENV FLASK_APP=app.py
    ENV FLASK_RUN_HOST=0.0.0.0


    
    # Run test.py when the container launches
    CMD ["python", "app.py"]
