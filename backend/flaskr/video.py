# RESTful API
from flask_restx import Namespace, Resource, fields
from function.video import uploads
from function.video.qiniu import upload,exist,get_token
from function.recommendation.recommendation import test,recommend_tag,recommend_video
from flask import request
import time 

import json 

api = Namespace('video', description='视频管理相关接口')
parser = api.parser()
parser.add_argument('name', type=str, help='名称')

video = api.parser()
video.add_argument('name', type=str, help='名称')
video.add_argument('video', type=str, help='视频文件')

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
    @api.expect(parser)
    @api.doc(description='根据所给名称生成token')
    def post(self):
        args = parser.parse_args()
        name = args['name']
        return get_token(name)
    

@api.route('/exist')
class exist_(Resource):
    @api.expect(parser)
    @api.doc(description='检验该文件名是否存在于储存空间中')
    def exist(self):
        args = parser.parse_args()
        name = args['name']
        return exist(name)
    @api.expect(parser)
    @api.doc(description='检验该文件名是否存在于储存空间中')
    def post(self):
        args = parser.parse_args()
        name = args['name']
        return exist(name)
    
@api.route('/uploads')
class upload(Resource):
    @api.expect(video)
    @api.doc(description='将视频进行上传，并以对应名称进行保存')
    def exist(self):
        args = video.parse_args()
        name = args['name']
        video = args['video']
        return uploads(name)
    @api.expect(video)
    @api.doc(description='将视频进行上传，并以对应名称进行保存')
    def post(self):
        args = video.parse_args()
        name = args['name']
        video = args['video']
        return uploads(name)

@api.route('/recommend')
class recommend(Resource):
    def post(self,data):
        return 