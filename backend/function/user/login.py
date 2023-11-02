from function.sql.data_get import get_value 
from werkzeug.security import check_password_hash
from flask import session

def login_(data):
    '''通过视频的名称来获取对应的token\n
    input:\n
        name  :  视频的名称\n
    output:\n
        data : josn文件\n
        data/ret : 状态码\n
        data/info : 具体信息(str)\n
    '''
    email = data["email"]
    password = data["password"]
    user = get_value(email,"email","User")
    if not user:
        return "未找到邮箱，请检测输入是否有误"
    if check_password_hash(user.password, password):
        # 将用户id保存到cookie：
        session['user_id'] = user.id
        return "登录成功"
    else:
        return "密码错误"

