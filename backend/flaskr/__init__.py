from flask import Flask, render_template
from flask_socketio import SocketIO
# 跨域
from flask_cors import CORS

# RESTful API
from flask_restx import Api
from function.user.exts import mail 

def create_app():
    global socketio
    app = Flask(__name__, instance_relative_config=True)
    # 跨域
    CORS(app, supports_credentials=True)
   
    socketio = SocketIO(app)
    api = Api(app, version='1.0', title='ShortVideo  API', description='短视频后端接口文档')

    # 从 config.py 文件中读取配置
    app.config.from_pyfile('flask_config.py')    
    mail.init_app(app)
    # 导入并注册命名空间
    from . import video,live,user
    api.add_namespace(video.api)
    api.add_namespace(live.api)
    api.add_namespace(user.api)



    if __name__ == "__main__":
        app.run(debug=True, host="0.0.0.0", port=50000)

    return app,socketio