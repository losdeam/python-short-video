# RESTful API
from flask_restx import Namespace, Resource, fields
from function.live_broadcast.live_init import create,close,join,leave
from function.live_broadcast.live_push import push,force_close,force_warning
from flask import request

from flaskr import socketio
import time 
import json 

api = Namespace('live', description='视频管理相关接口')

# get的视频链接获取接口
@api.route('/live_create')
class live_create(Resource):
    def post(self):
        data = request.get_json() 
        return create(data)
# 生成上传所需的token
@api.route('/live_close')
class live_close(Resource):
    def post(self):
        data = request.get_json() 
        return close(data,socketio)
# 生成上传所需的token
@api.route('/live_join')
class live_join(Resource):
    def post(self):
        data = request.get_json() 
        return join(data)
# 生成上传所需的token
@api.route('/live_leave')
class live_leave(Resource):
    def post(self):
        data = request.get_json() 
        return leave(data)
