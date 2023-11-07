from flask_login import current_user

from function.sql import get_value
from flaskr.extensions import redis_client


def get_like(video_id):
    '''
    用户点赞具体实现
    '''
    # 验证video_id是否存在
    if get_value(video_id, 'video_id', 'video') is None:
        return {'massage': '视频不存在'}, 404

    # 使用Redis的集合来存储视频点赞信息，集合的名称可以以视频ID为前缀
    like_video_key = 'like_video:' + str(video_id)

    # 使用列表来存储用户点赞信息，列表的名称可以以用户ID为前缀
    like_user_key = 'like_user:' + str(current_user.user_id)  # type: ignore

    # 检查用户是否已经点赞，如果已经点赞则取消点赞
    if redis_client.sismember(like_video_key, current_user.user_id):    # type: ignore
        redis_client.srem(
            like_video_key, current_user.user_id)   # type: ignore
        redis_client.lrem(like_user_key, 1, video_id)
    else:
        redis_client.sadd(like_video_key, current_user.user_id)  # type: ignore
        redis_client.lpush(like_user_key, video_id)
        redis_client.ltrim(like_user_key, 0, 20)  # 保留最近的20个视频ID

    # 返回点赞总数
    num = redis_client.scard(like_video_key)

    return num, 200


def get_like_history(user_id):
    '''
    用户点赞历史, 最近十个，具体实现
    '''
    # 获取用户点赞过的视频ID集合
    like_user_key = 'like_user:' + str(user_id)
    # 返回最近十个视频ID
    video_ids = redis_client.lrange(like_user_key, 0, 9)

    # 将列表转化为json格式
    video_ids = [int(video_id) for video_id in video_ids]

    # 如果video_ids为空
    if len(video_ids) == 0:
        return {'massage': '没有点赞历史'}, 404

    return video_ids, 200


def get_watch_history():
    '''
    用户历史记录具体实现
    '''
    # 获取用户浏览过的视频ID列表
    history_user_key = 'history_user:' + \
        str(current_user.user_id)  # type: ignore

    # 返回全部历史记录
    video_ids = redis_client.lrange(history_user_key, 0, -1)

    # 将列表转化为json格式
    video_ids = [int(video_id) for video_id in video_ids]

    # 如果video_ids为空
    if len(video_ids) == 0:
        return {'massage': '没有历史记录'}, 404

    return video_ids, 200
