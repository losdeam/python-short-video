from flaskr.extensions import db
from flaskr.models import User, Video


def upload_data(data, sheet):
    '''
    data:dict
    sheet:str
    将data中的数据上传数据库的sheet表中
    '''
    if sheet == 'user':
        stmt = db.insert(User).values(data)
    elif sheet == 'video':
        stmt = db.insert(Video).values(data)
    else:
        raise AttributeError("sheet name error")

    db.session.execute(stmt)
    db.session.commit()

    pass


# 获取最近用户访问最多的tag(拓展：同时获取热门tag，以随机数的形式获取为当前用户推荐的视频tag)
def get_tag():
    pass

# 获取对应tag的视频列表


def get_video():
    pass


def get_value(data, key, sheet):
    '''
    根据所给的data值在sheet的key字段中寻找一条记录
    return : 字典格式的记录,不存在则返回None
    '''
    if sheet == 'user':
        stmt = db.select(User).where(getattr(User, key) == data)
    elif sheet == 'video':
        stmt = db.select(Video).where(getattr(Video, key) == data)
    else:
        raise AttributeError("sheet name error")

    result = db.session.execute(stmt).scalar_one_or_none()

    return result


def get_values(data, key, sheet):
    '''
    根据所给的data值在sheet的key字段中寻找所有符合的记录
    return : 字典格式的记录,不存在则返回None
    '''
    if sheet == 'user':
        stmt = db.select(User).where(getattr(User, key) == data)
    elif sheet == 'video':
        stmt = db.select(Video).where(getattr(Video, key) == data)
    else:
        raise AttributeError("sheet name error")

    result = db.session.execute(stmt).scalars().all()

    if result:
        return result
    else:
        return None
