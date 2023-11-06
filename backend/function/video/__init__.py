from .load import load
from .qiniu import upload, exist, get_token, verify, delete, get
from function.sql import get_value, upload_data


def pre(user, name):
    return user + "_" +name


def upload_(user, video, name,image):
    name = pre(user, name)
    return upload(name, video,image)


def exist_(user, name, buckets):
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


def get_(id,prefix, buckets):
    return get(prefix, buckets)
