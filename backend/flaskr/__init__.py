from flask import Flask
# 跨域
from flask_cors import CORS
# RESTful API
from flask_restx import Api
# 导入需要初始化的组件
from flaskr.extensions import db, socketio, mail, login_manager


def create_app():
    # 创造并配置app, instance_relative_config=True表示配置文件是相对于instance folder的相对路径
    app = Flask(__name__, instance_relative_config=True)

    # RESTful API
    api = Api(app, version='1.0', title='ShortVideo  API',
              description='短视频后端接口文档', prefix='/api')

    # 跨域
    CORS(app, supports_credentials=True)

    # 从 config.py 文件中读取配置
    app.config.from_pyfile('config.py')

    # 初始化各种组件
    db.init_app(app)
    socketio.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)

    # 导入并注册命名空间
    from . import live, database, auth, video_manage
    api.add_namespace(database.api)
    api.add_namespace(video_manage.api)
    api.add_namespace(live.api)
    api.add_namespace(auth.api)

    if __name__ == "__main__":
        socketio.run(app, debug=True, host="0.0.0.0", port=50000,
                     use_reloader=True, log_output=True)

    return app
