from .load import load
from .qiniu import upload, exist, get_token, verify, delete, get
from function.sql import get_value, upload_data


def pre(user, name):
    return user + name


def upload_(user, video, name):
    name = pre(user, name)
    return upload(name, video)


def exist_(user, name, buckets):
    if get_value("test", 'user', "username"):
        print(1)
    name = pre(user, name)
    return exist(name, buckets)


def get_token_(user, name):
    name = pre(user, name)
    return get_token(name)


def verify_(user, name):
    name = pre(user, name)
    return verify(name)


def delete_(user, name, bucketname):
    name = pre(user, name)
    return delete(name, bucketname)


def get_(user, prefix, buckets):
    return get(prefix, buckets)
