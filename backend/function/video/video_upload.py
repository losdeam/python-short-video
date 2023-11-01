

from qiniu import Auth, put_data, etag
import qiniu.config

def upload(name):
    #需要填写你的 Access Key 和 Secret Key
    access_key = 'JBmGTOlz7n8YQ4UQ3uqXvAEo9A9dMaw1eC1VOBKw'
    secret_key = 'd_Wf18TVRIq1NouNvqYIwFngaV90gxiEi26YxyLw'

    #构建鉴权对象
    q = Auth(access_key, secret_key)

    #要上传的空间
    bucket_name = 'zeros'

    #上传后保存的文件名
    key = name

    #生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)

    return token
