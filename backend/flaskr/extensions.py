# 导入各种拓展
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_mail import Mail
from flask_login import LoginManager
from flask_redis import FlaskRedis


# 实例化
db = SQLAlchemy()
socketio = SocketIO()
mail = Mail()
login_manager = LoginManager()
redis_client = FlaskRedis()
