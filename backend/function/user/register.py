
from flask_mail import Message
import string
import random
import re
from  time import sleep 
from werkzeug.security import generate_password_hash

from .exts import mail
from function.sql.data_judge import exist 
from function.sql import upload

times = 120 # 验证码保留秒数
email_dict= {}
# 获取并发送验证码，并临时建立邮箱与验证码的映射
def get_email_captcha(email):
    global email_dict
    # 4/6：随机数组、字母、数组和字母的组合
    source = string.hexdigits*4
    captcha = random.sample(source, 4)
    captcha = "".join(captcha)
    # I/O：Input/Output
    message = Message(subject="注册验证码", recipients=[email], body=f"您的验证码是:{captcha},仅在两分钟内有效")
    mail.send(message)
    email_dict[email] = captcha
    sleep(times)
    if email in email_dict:
        del email_dict[email]

def regist(data):
    '''
        data:前端返回的json数据
        data/name :用户名
        data/password :密码
        data/email :邮箱
        data/captcha :验证码
    '''

    name = data["name"]
    password = data["password"]
    email = data["email"]
    captcha = data["captcha"]
    if exist(data,"User","usernmae"):
        return False,"用户名已存在"
    if email_dict[email] != captcha:
        return False,"验证码错误"
    flag,msg = check_password_secure(password)
    password = generate_password_hash(password)
    if not flag :
        return flag,msg 
    upload({"name":name,"password":password,"email":email,"captcha":captcha},"User")
    return flag,msg 
    


def test():
    print(email_dict)


def check_password_secure(password):
    '''
    密码安全性判断
    return： flag: 是否可行
            msg : 不可行的话给出原因，可行返回密码安全性
    '''
    # 初始化分数
    score = 0
    # 长度判定
    length = len(password)
    if length < 8:
        return  False,"密码长度至少需要8位"
    else:
        score += length
    # 字符类型判定
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digits = re.search(r'[0-9]', password)
    has_symbol = re.search(r'[ !#$%&\'()*+,-./[\\\]^_`{|}~"+:=?]', password)
    char_types = [1  if i else 0  for i in (has_upper, has_lower,has_digits, has_symbol) ]
    if sum(char_types) < 2:
        return  False,"密码需要包含多种字符类型"
    else:
        score += 10 * sum(char_types)
    # 常见密码或日期判定
    if password.lower() in ['password', '123456'] or re.match(r'\d{4,}', password):
        return  False,"密码不能是常见密码或连续数字"
    if score >= 45:
        return  True,"非常安全的密码"
    elif score >= 30:
        return  True,"安全性一般的密码"


