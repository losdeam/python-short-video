from flask import Flask, render_template
from flask_socketio import SocketIO
# 跨域
from flask_cors import CORS

# RESTful API
from flask_restx import Api

# 创造并配置app, instance_relative_config=True表示配置文件是相对于instance folder的相对路径
app = Flask(__name__, instance_relative_config=True)
socketio = SocketIO(app)
api = Api(app, version='1.0', title='ShortVideo  API', description='短视频后端接口文档')
   
def create_app():

    # 跨域
    CORS(app, supports_credentials=True)

    # 从 config.py 文件中读取配置
    app.config.from_pyfile('flask_config.py')    

    # 导入并注册命名空间
    from . import video,live
    # RESTful API

    api.add_namespace(video.api)
    api.add_namespace(live.api)



    if __name__ == "__main__":
        app.run(debug=True, host="0.0.0.0", port=50000)

    return app,socketio

if __name__ == "__main__":
    create_app()