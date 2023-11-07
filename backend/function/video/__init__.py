from .qiniu import upload, get_token, verify, delete, get
from .video import get_sort, get_video


def pre(user, name):
    return user + "_" + name


def upload_(user, video, name, image):
    name = pre(user, name)
    return upload(name, video, image)


def get_token_(user, name):
    name = pre(user, name)
    return get_token(name)


def verify_(user, name):
    name = pre(user, name)
    return verify(name)


def delete_(user, name, bucketname):
    name = pre(user, name)
    return delete(name, bucketname)


def get_(id, prefix, buckets):
    return get(prefix, buckets)
