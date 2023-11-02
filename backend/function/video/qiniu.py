from qiniu import  etag,BucketManager, put_data, etag, urlsafe_base64_encode
from instance.qny_cofig import q,bucket_name  ,pipeline,fops,temp_bucket
from flask import jsonify


def get_token(name):
    '''通过视频的名称来获取对应的token\n
    input:\n
        name  :  视频的名称\n
    output:\n
        data : josn文件\n
        data/ret : 状态码\n
        data/info : 具体信息(str)\n
    '''
    print(type(name))
    print(name )
    data = { }
    #上传后保存的文件名
    key = name
    if not exist(name):
        #生成上传 Token，可以指定过期时间等
        token = q.upload_token(bucket_name, key, 3600)
        data["ret"] = 200
        data["info"] = token
        
    else:
        data["ret"] = 404
        data["info"] = "已存在相同文件名的视频"
    return  jsonify(data)


def upload (name,video):
    '''处理完成的视频数据,并上传到临时的储存空间中等待审核\n
    input:\n
        name  :  视频的名称\n
        video :  二进制的视频文件\n
    output:\n
        data : josn文件\n
        data/ret : 状态码\n
        data/info : 具体信息\n
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
        data["info"] = info
    else:
        data["ret"] = False
        data["info"] = "已存在相同文件名的视频"

    return jsonify(data)



def exist(name):
    '''验证该名称在储存空间中是否已经存在\n
    input:\n
        name  :  视频的名称\n
    output:\n
        data : josn文件\n
        data/ret : 状态码\n
        data/info : 具体信息\n
    '''
    data = {}
    bucket = BucketManager(q)
    ret, info = bucket.stat(bucket_name, name)
    data["ret"] = ret
    if ret:
        data["info"] = "该名称在储存空间中已经存在"
        return  jsonify(data)
    else :

        data["info"] = "该名称在储存空间中不存在"
        return jsonify(data)