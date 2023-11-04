# RESTful API
from flask_restx import Namespace, Resource
from function.user import get_email_captcha,test,login_,regist

api = Namespace('user', description='用户管理相关接口')
parser = api.parser()
parser.add_argument('name', type=str, help='名称')
parser.add_argument('password', type=str, help='密码')
parser.add_argument('email', type=str, help='邮箱')
parser.add_argument('captcha', type=str, help='验证码')

parser_login = api.parser()
parser_login.add_argument('email', type=str, help='邮箱')
parser_login.add_argument('password', type=str, help='密码')

# 验证码发送接口
@api.route('/user_get_email_captcha')
class user_get_email_captcha(Resource):
    @api.doc(description='注册时，\
             发送验证码。')
    @api.expect(parser)
    def post(self):
        args = parser.parse_args()
        email = args['email']
        return get_email_captcha(email)

@api.route('/register')
class register(Resource):
    @api.expect(parser)
    @api.doc(description='注册，\
            输入  name :用户名，password :密码，email :邮箱，captcha :验证码。')
    def post(self):
        args = parser.parse_args()
        return regist(args)
    
@api.route('/login')
class login(Resource):
    @api.expect(parser_login)
    @api.doc(description='登录，\
            输入  email :邮箱，password :密码')
    def post(self):
        parser_login = parser.parse_args()
        return login_(parser_login)

@api.route('/test')
class test_(Resource):
        
    @api.doc(description='测试，\
            输出内存中所有邮箱与验证码的映射。')
    def post(self):
        return test()
