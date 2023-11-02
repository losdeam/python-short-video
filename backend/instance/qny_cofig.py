from qiniu import Auth
#需要填写你的 Access Key 和 Secret Key
access_key = 'JBmGTOlz7n8YQ4UQ3uqXvAEo9A9dMaw1eC1VOBKw'
secret_key = 'd_Wf18TVRIq1NouNvqYIwFngaV90gxiEi26YxyLw'
#构建鉴权对象
q = Auth(access_key, secret_key)
#要上传的空间
bucket_name = 'zeros'
# 暂存的空间
temp_bucket = "zerotemp"


#设置转码参数
fops = 'avthumb/mp4/s/640x360/vb/1.25m'
#转码是使用的队列名称
pipeline = 'abc'