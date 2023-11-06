
from instance.qny_config import q, bucket_name, pipeline, fops, temp_bucket, bucket
from qiniu import etag, put_data, urlsafe_base64_encode,put_file
from flask import jsonify
import json

def get_token(name):
    '''通过视频的名称来获取对应的token\n
    input:\n
        name  :  视频的名称\n
    output:\n
        data : josn文件\n
        data/ret : 储存空间中的视频信息，若无则返回NULL\n
        data/code : 状态码\n
        data/info : 具体信息(str)\n
        code : 状态码\n
    '''
    data = {}
    # 上传后保存的文件名
    key = name
    
    ret, response = exist(name, temp_bucket)
    data["ret"] = ret["ret"]
    if response == 404:
        # 生成上传 Token，可以指定过期时间等
        token = q.upload_token(bucket_name, key, 3600)
        data["code"] = 200
        data["info"] = token
    else:
        data["code"] = 404
        data["info"] = "已存在相同文件名的视频"
    return data, data["code"]


def upload(name, video,image):
    '''处理完成的视频数据,并上传到临时的储存空间中等待审核\n
    input:\n
        name  :  视频的名称\n
        video :  网页传回的视频文件\n
        image : 网页传回的封面文件\n
    output:\n
        data : josn文件\n
        data/ret : 储存空间中的视频信息，若无则返回NULL\n
        data/code : 状态码\n
        data/info : 具体信息(str)\n
        code : 状态码\n
    '''
    data = {}
    video_name = name + ".mp4"
    image_name = name + ".jpg"

    ret, info = bucket.stat(bucket_name, video_name)

    if not ret:
        # 可以对转码后的文件进行使用saveas参数自定义命名，当然也可以不指定文件会默认命名并保存在当前空间
        token_video = q.upload_token(temp_bucket, video_name, 3600)
        ret, info = put_data(token_video, video_name, video)
        
        token_image = q.upload_token(temp_bucket, image_name, 3600)
        ret, info = put_data(token_image, image_name, image) 
        
        data["ret"] = ret
        data["code"] = 200
        data["info"] = "上传成功"
    else:
        data["ret"] = None
        data["code"] = 404
        data["info"] = "已存在相同文件名的视频"
    return jsonify(data), data["code"]



def exist(name, buckets):
    '''验证该名称在储存空间中是否已经存在\n
    input:\n
        name  :  视频的名称\n
    output:\n
        data : josn文件\n
        data/ret : 储存空间中的视频信息，若无则返回NULL\n
        data/code : 状态码\n
        data/info : 具体信息(str)\n
        code : 状态码\n
    '''

    bucketname,private_url = find_url(name, buckets)
    data = {}
    ret, info = bucket.stat(bucketname, name)
    data["ret"] = ret
    if ret:
        data["code"] = 200
        data["info"] = private_url
    else:
        data["code"] = 404
        data["info"] = "该名称在储存空间中不存在"
    return data, data["code"]


def verify(name):
    '''管理员审核对应视频，并给予通过\n
    input:\n
        name  :  视频的名称\n
    output:\n
        data : josn文件\n
        data/code : 状态码\n
        data/info : 具体信息(str)\n
        code : 状态码\n
    '''
    name_video = name + ".mp4"
    name_image = name + ".jpg"
    ret, info = bucket.stat(temp_bucket, name)
    
    data = {}
    if ret :
        ret, info = bucket.move(temp_bucket, name_video, bucket_name, name_video)
        ret, info = bucket.move(temp_bucket, name_image, bucket_name, name)
        data["code"] = 200
        data["info"] = "审核成功，视频将转移至正式空间中"
    else:
        data["code"] = 404
        data["info"] = "审核失败，视频不存在于该空间中"

    return data, data["code"]


def delete(name, buckets):
    '''用户或管理员删除对应视频\n
    input:\n
        name  :  视频的名称\n
        buckets : 储存空间名称（1为正式空间，0为中转空间）\n
    output:\n    
        data : josn文件\n
        data/code : 状态码\n
        data/info : 具体信息(str)\n
        code : 状态码\n
    '''
    data = {}
    name_video = name + ".mp4"
    name_image = name + ".jpg"
    if buckets :
        bucketname = bucket_name
    else:
        bucketname = temp_bucket
    _, ret = exist(name, bucketname)
    if ret == 200:
        ret, info = bucket.delete(bucketname, name_video)
        ret, info = bucket.delete(bucketname, name_image)
        data["code"] = 200
        data["info"] = "删除成功"
    else:
        data["code"] = 404
        data["info"] = "该名称在储存空间中不存在"
    return data, data["code"]


def get(prefix, buckets):
    '''根据前缀查询对应空间中的视频\n
    input:\n
        prefix  :  视频前缀名\n
        buckets : 储存空间名称（1为正式空间，0为中转空间）\n
    output:\n    
        data : josn文件\n
        data/code : 状态码\n
        data/info : 具体信息(str)\n
        code : 状态码\n
    '''
    data = {}
    if buckets :
        bucket_ = bucket_name
    else:
        bucket_ = temp_bucket
    # 前缀
    prefix = prefix
    # 列举条目
    limit = 10
    # 列举出除'/'的所有文件以及以'/'为分隔的所有前缀
    delimiter = "_"
    # 标记
    marker = None

    ret, _, _ = bucket.list(bucket_, prefix, marker, limit, delimiter)
    data["ret"] = ret
    data["code"] = 200
    data["bucket"] = bucket_
    return data, data["code"]


def find_url(name,buckets):
    if buckets:
        bucket_domain = "s360yyqhm.hn-bkt.clouddn.com"
        bucketname = bucket_name
    else:
        bucket_domain = "s3hoslajq.hn-bkt.clouddn.com"
        bucketname = temp_bucket
    base_url = 'http://%s/%s' % (bucket_domain, name)
    private_url = q.private_download_url(base_url, expires=3600)
    return bucketname,private_url
