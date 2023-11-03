from qiniu import  etag, put_data, urlsafe_base64_encode
from instance.qny_cofig import q,bucket_name  ,pipeline,fops,temp_bucket,bucket
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
    data = { }
    #上传后保存的文件名
    key = name
    ret , response = exist(name)
    data["ret"] = ret["ret"]
    if response == 404 :
        #生成上传 Token，可以指定过期时间等
        token = q.upload_token(bucket_name, key, 3600)
        data["code"] = 200
        data["info"] = token
    else:
        data["code"] = 404
        data["info"] = "已存在相同文件名的视频"
    return  data ,data["code"]

def upload (name,video):
    '''处理完成的视频数据,并上传到临时的储存空间中等待审核\n
    input:\n
        name  :  视频的名称\n
        video :  二进制的视频文件\n
    output:\n
        data : josn文件\n
        data/ret : 储存空间中的视频信息，若无则返回NULL\n
        data/code : 状态码\n
        data/info : 具体信息(str)\n
        code : 状态码\n
    '''
    data = {}
    if not exist(name):
        #生成上传 Token，可以指定过期时间等
        fops = fops
        #可以对转码后的文件进行使用saveas参数自定义命名，当然也可以不指定文件会默认命名并保存在当前空间
        saveas_key = urlsafe_base64_encode(f'{temp_bucket}:{name}')
        fops = fops+'|saveas/'+saveas_key
        #在上传策略中指定
        policy={
        'persistentOps':fops,
        'persistentPipeline':pipeline
        }
        token = q.upload_token(bucket_name, name, 3600, policy)
        ret, info = put_data(token, name, video, version='v2') 
        data["ret"] = ret
        data["code"] = 200
        data["info"] = info

    else:
        data["ret"] = None
        data["code"] = 404
        data["info"] = "已存在相同文件名的视频"
    return  jsonify(data) ,data["code"] 

def exist(name):
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
    data = {}
    
    ret, info = bucket.stat(bucket_name, name)
    data["ret"] = ret
    if ret:
        data["code"] = 200
        data["info"] = "该名称在储存空间中已经存在"
        
    else :
        data["code"] = 404
        data["info"] = "该名称在储存空间中不存在"
    return  data , data["code"]

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
    
    ret, info = bucket.move(temp_bucket, name, bucket_name, name)
    data = {}
    if ret:
        ret, info = bucket.delete(temp_bucket, name)
        data["code"] = 200
        data["info"] = "成功审核，视频将转移至正式空间中"
    else :
        data["code"] = 404
        data["info"] = "该名称在储存空间中不存在"
    return  data , data["code"]

def delete(name,bucketname):
    '''用户或管理员删除对应视频\n
    input:\n
        name  :  视频的名称\n
    output:\n    
        data : josn文件\n
        data/code : 状态码\n
        data/info : 具体信息(str)\n
        code : 状态码\n
    '''
    ret, info = bucket.delete(bucketname, name)
    data = {}
    if ret:
        data["code"] = 200
        data["info"] = "删除成功"
    else :
        data["code"] = 404
        data["info"] = "该名称在储存空间中不存在"
    return  data , data["code"]