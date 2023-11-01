# RESTful API
from flask_restx import Namespace, Resource
from function.user import get_email_captcha,test,login_,regist

api = Namespace('user', description='用户管理相关接口')

# 验证码发送接口
@api.route('/user_get_email_captcha')
class user_get_email_captcha(Resource):
    @api.doc(description='注册时，\
             发送验证码。')
    def post(self):
        email = api.payload['email']
        return get_email_captcha(email)

@api.route('/register')
class register(Resource):
    @api.doc(description='注册，\
            输入  name :用户名，password :密码，email :邮箱，captcha :验证码。')
    def post(self):
        return regist()
    
@api.route('/login')
class login(Resource):
    @api.doc(description='登录，\
            输入  email :邮箱，password :密码')
    def post(self):
        return login_()

@api.route('/test')
class test_(Resource):
    @api.doc(description='测试，\
            输出内存中所有邮箱与验证码的映射。')
    def post(self):
        return test()
