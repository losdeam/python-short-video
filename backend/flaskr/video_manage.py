# RESTful API
from flask_restx import Namespace, Resource, fields
from flask import request, jsonify
from flask_login import login_required, current_user  # 用户认证

from flaskr.models import User, Video
from function.video import upload_, exist_, get_token_, verify_, delete_, get_
from function.recommendation.recommendation import test, recommend_tag, recommend_video


api = Namespace('video', description='视频管理相关接口')


video_model = api.model('VedioModel', {
    "title": fields.String(required=True, description='视频标题'),
    "video_url": fields.String(required=True, description='视频地址'),
    "sort": fields.String(required=True, description='视频分类')
})


@api.route('/videos')
class Videos(Resource):
    def get(self):
        data = {
            "message": "Hi.AirCode",
            "src": "http://s360yyqhm.hn-bkt.clouddn.com/1.mp4"
        }
        return jsonify(data)


@api.route('/token_get')
class token_get(Resource):
    @api.doc(description='根据所给名称生成token')
    def post(self):
        payload = request.get_json()
        user = payload.get('id')
        name = payload.get('name')
        return get_token_(user, name)


@api.route('/exist')
class exist(Resource):
    @api.doc(description='检验该文件名是否存在于储存空间中')
    def post(self):
        payload = request.get_json()
        user = payload.get('id')
        name = payload.get('name')
        buckets = payload.get('buckets')
        return exist_(user, name, buckets)


@api.route('/uploads')
class Upload(Resource):
    @api.doc(description='将视频进行上传，并以对应名称进行保存')
    def post(self):
        payload = request.get_json()
        user = payload.get('id')
        name = payload.get('name')
        video = payload.get('video')
        image = payload.get('image')
        return upload_(user, video, name,image)


@api.route('/recommend')
class recommend(Resource):
    def post(self):
        return


@api.route('/verify')
class verify(Resource):
    @api.doc(description='审核员对中转站的视频进行审核')
    def post(self):

        payload = request.get_json()
        user = payload.get('id')
        name = payload.get('name')
        return verify_(user, name)


@api.route('/delete')
class delete(Resource):
    @api.doc(description='具有权限的用户删除对应空间中的视频')
    def post(self):
        payload = request.get_json()
        user = payload.get('id')
        name = payload.get('name')
        bucketname = payload.get('bucketname')
        return delete_(user, name, bucketname)


@api.route('/search')
class get(Resource):
    @api.doc(description='查找对应前缀的视频')
    def post(self):
        payload = request.get_json()
        user = payload.get('id')
        prefix = payload.get('prefix')
        buckets = payload.get('name')
        return get_(user, prefix=prefix, buckets=buckets)
