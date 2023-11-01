# RESTful API
from flask_restx import Namespace, Resource, fields
from function.user.register import get_email_captcha,test

from flask import request

from flaskr import socketio
import time 
import json 

api = Namespace('user', description='用户管理相关接口')

# 验证码发送接口
@api.route('/user_get_email_captcha')
class user_get_email_captcha(Resource):
    @api.doc(description='注册时，\
             发送验证码。')
    def post(self):
        email = api.payload['email']
        return get_email_captcha(email)
    def get(self):
        email = api.payload['email']
        return get_email_captcha(email)
    

@api.route('/test')
class test_(Resource):
    @api.doc(description='测试，\
            输出内存中所有邮箱与验证码的映射。')
    def post(self):
        return test()
