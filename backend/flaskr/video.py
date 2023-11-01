# RESTful API
from flask_restx import Namespace, Resource, fields
from function.video.video_upload import upload
from function.recommendation.recommendation import test,recommend_tag,recommend_video
from flask import request
import time 
import json 

api = Namespace('video', description='视频管理相关接口')


# get的视频链接获取接口
@api.route('/test_1')
class test_1(Resource):
    def get(self):
        data = {
            "message" : "Hi.AirCode",
            "src" : "http://s360yyqhm.hn-bkt.clouddn.com/1.mp4"
        }
        return json.dumps(data)

# 生成上传所需的token
@api.route('/token_get')
class token_get(Resource):
    def post(self):
        data = request.get_json() 
        return upload(data["name"])
    
@api.route('/test')
class test_(Resource):
    def get(self):
        
        return test()
    
@api.route('/recommend')
class recommend(Resource):
    def post(self,data):
        return 
