
from flask import jsonify
from flask_mail import Message
from flask import request
import string
import random
from flask_mail import Mail
from werkzeug.security import generate_password_hash, check_password_hash


def get_email_captcha(email):
    # /captcha/email/<email>
    # /captcha/email?email=xxx@qq.com
    email = request.args.get("email")
    # 4/6：随机数组、字母、数组和字母的组合
    source = string.digits*4
    captcha = random.sample(source, 4)
    captcha = "".join(captcha)
    mail = Mail()
    # I/O：Input/Output
    message = Message(subject="注册验证码", recipients=[email], body=f"您的验证码是:{captcha}")
    mail.send(message)
    # RESTful API
    # {code: 200/400/500, message: "", data: {}}
    return jsonify({"code": 200, "message": "", "data": None})


