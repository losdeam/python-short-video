# RESTful API
from flask_restx import Namespace, Resource, fields
from flask import request, jsonify
from flask_login import login_required, current_user  # 用户认证

from function.video import upload, get_video, get_token_, verify_, delete_, get_sort, get_


api = Namespace('video', description='视频管理相关接口')


video_model = api.model('VedioModel', {
    'title': fields.String(required=True, max_length=100, description='视频标题'),
    'video_url': fields.String(required=True, max_length=255, description='视频地址'),
    'sort': fields.String(required=True, max_length=50, description='视频分类')
})

all_video_model = api.clone('AllVideoModel', video_model, {
    'user_id': fields.Integer(required=True, description='用户ID'),
    'description': fields.String(required=True, description='视频描述'),
    'upload_date': fields.DateTime(required=True, description='上传日期')
})


# @api.route('/videos')
# class AllVideos(Resource):

@api.route('/videos/<int:video_id>')
class Videos(Resource):
    @api.doc(description='获取视频信息，并记录浏览历史，浏览历史每满十个，就重新计算推荐视频')
    def get(self, video_id):
        '''
        获取视频信息
        '''
        # data = {
        #     "message": "Hi.AirCode",
        #     "src": "http://s360yyqhm.hn-bkt.clouddn.com/1.mp4"
        # }

        return get_video(video_id)


@api.route('/sortvideos/<string:sort>')
class SortVideos(Resource):
    @api.doc(description='获取对应分类的视频列表')
    @api.marshal_with(all_video_model)
    @login_required
    def get(self, sort):
        '''
        获取分类视频列表
        '''
        return get_sort(sort)


@api.route('/token_get')
class token_get(Resource):
    @api.doc(description='根据所给名称生成token')
    def post(self):
        payload = request.get_json()
        user = payload.get('id')
        name = payload.get('name')
        return get_token_(user, name)


@api.route('/uploads')
class Upload(Resource):
    @api.doc(description='将视频进行上传，并以对应名称进行保存')
    def post(self):
        payload = request.get_json()
        user = payload.get('id')
        name = payload.get('name')
        video = payload.get('video')
        image = payload.get('image')
        return upload_(user, video, name, image)


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
