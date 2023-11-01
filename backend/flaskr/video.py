# RESTful API
from flask_restx import Namespace, Resource, fields


api = Namespace('video', description='视频管理相关接口')