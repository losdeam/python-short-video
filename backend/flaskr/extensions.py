# 导入各种拓展
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

# 实例化
db = SQLAlchemy()
socketio = SocketIO()
