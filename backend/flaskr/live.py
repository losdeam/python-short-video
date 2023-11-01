# RESTful API
from flask_restx import Namespace, Resource, fields
from function.live_broadcast.live_init import create,close,join,leave
from function.live_broadcast.live_push import push,force_close,force_warning
from flask import request

from flaskr import socketio
import time 
import json 

api = Namespace('live', description='直播管理相关接口')

# get的视频链接获取接口
@api.route('/live_create')
class live_create(Resource):
    @api.doc(description='主播，创建直播间')
    def post(self):
        data = request.get_json() 
        return create(data)
# 生成上传所需的token
@api.route('/live_close')
class live_close(Resource):
    @api.doc(description='主播，关闭直播间')
    def post(self):
        data = request.get_json() 
        return close(data,socketio)
# 生成上传所需的token
@api.route('/live_join')
class live_join(Resource):
    @api.doc(description='观众，进入直播间')
    def post(self):
        data = request.get_json() 
        return join(data)
# 生成上传所需的token
@api.route('/live_leave')
class live_leave(Resource):
    @api.doc(description='观众，离开直播间')
    def post(self):
        data = request.get_json() 
        return leave(data)
    
@api.route('/live_push')
class live_push(Resource):
    @api.doc(description='主播，直播间视频推流')
    def post(self):
        data = request.get_json() 
        return push(data,socketio)
    
@api.route('/live_force_close')
class live_force_close(Resource):
    @api.doc(description='房管，强制关闭直播间')
    def post(self):
        data = request.get_json() 
        return force_close(data)
    
@api.route('/live_force_warning')
class live_force_warning(Resource):
    @api.doc(description='房管，警告直播间')
    def post(self):
        data = request.get_json() 
        return force_warning(data,socketio)
