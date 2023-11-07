from flask_restx import Namespace, Resource, fields
from flask_login import login_required

from function.operate import get_like, get_like_history, get_watch_history
from function.recommendation.recommendation import test, recommend_tag, recommend_video
from function.recommendation.data_processing import dataread


api = Namespace('operate', description='用户操作相关接口')


user_id_model = api.model('UserIdModel', {
    'user_id': fields.Integer(required=True, description='用户id')
})


@api.route('/like')
class AllLike(Resource):
    @api.doc(description='用户历史点赞,返回最近的十个')
    @api.expect(user_id_model, validate=True)
    @login_required
    def post(self):
        '''
        用户点赞历史
        '''
        user_id = api.payload['user_id']
        return get_like_history(user_id)


@api.route('/like/<int:video_id>')
class Like(Resource):
    @api.doc(description='用户点赞功能,已点赞则取消点赞')
    @login_required
    def get(self, video_id):
        '''
        用户点赞
        '''
        return get_like(video_id)


@api.route('/watch')
class Watch(Resource):
    @api.doc(description='用户历史记录')
    @login_required
    def get(self):
        '''
        用户历史记录
        '''
        return get_watch_history()


@api.route('/dataread')
class dataread_(Resource):
    @api.doc(description='推荐系统训练数据读取功能')
    @login_required
    def post(self):
        '''
        推荐系统训练数据读取功能
        '''
        user_id = api.payload['user_id']
        return {"test": 1}, dataread(user_id)
