# RESTful API
from flask_restx import Namespace, Resource
from function.video.video_upload import upload
from function.recommendation.recommendation import test, recommend_tag, recommend_video
from flask import request, jsonify
import time
import json

api = Namespace('show', description='展示相关接口')


@api.route('/videos')
class Video(Resource):
    def get(self):
        data = {
            "message": "Hi.AirCode",
            "src": "http://s360yyqhm.hn-bkt.clouddn.com/1.mp4"
        }

        return jsonify(data)

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
    def post(self, data):
        return
