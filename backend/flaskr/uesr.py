# RESTful API
from flask_restx import Namespace, Resource, fields
from function.user.login import get_email_captcha

from flask import request

from flaskr import socketio
import time 
import json 

api = Namespace('user', description='用户管理相关接口')

# get的视频链接获取接口
@api.route('/user_get_email_captcha')
class user_get_email_captcha(Resource):
    def post(self):
        return get_email_captcha("3500166558@qq.com")
