
from .qiniu import upload, exist, get_token, verify, delete, get
from function.sql import get_value, upload_data, get_values


def pre(user, name):
    return user + name


def upload_(user, video, name):
    name = pre(user, name)
    return upload(name, video)


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


def get_(id, prefix, buckets):
    return get(prefix, buckets)


def get_sort(sort):

    result = get_values(sort, "sort", "video")
    # 理论上应该按热度排序
    # result.sort(reverse = True ,key = hot)
    t = []
    if result:
        # 排序完后提取
        for i in range(min(len(result), 50)):
            t .append(result[i].video_url)
    return result
