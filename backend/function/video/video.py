from flask_login import current_user

from flaskr.extensions import redis_client
from .qiniu import exist
from function.sql import get_value, get_values


def pre(user, name):
    return user + "_" + name


def get_video(video_id):
    '''
    获取视频信息具体实现
    '''
    # 验证video_id是否存在
    video_result = get_value(video_id, 'video_id', 'video')
    if video_result is None:
        return {'massage': '视频不存在'}, 404

    # 拼接视频name
    title = video_result.title
    user_id = video_result.user_id
    name = pre(user_id, title)

    # 使用Redis的列表来存储用户浏览历史，列表的名称可以以用户ID为前缀
    history_user_key = 'history_user:' + \
        str(current_user.user_id)  # type: ignore

    recommend_user_key = 'recommend_user:' + \
        str(current_user.user_id)  # type: ignore

    # 检查用户是否已经浏览过，如果已经浏览过则删除原来的浏览记录
    if redis_client.lrange(history_user_key, 0, -1):
        redis_client.lrem(history_user_key, 1, video_id)

    if redis_client.lrange(recommend_user_key, 0, -1):
        redis_client.lrem(recommend_user_key, 1, video_id)

    # 将视频ID插入到列表的最前面
    redis_client.lpush(history_user_key, video_id)
    redis_client.ltrim(history_user_key, 0, 30)  # 保留最近的30个视频浏览记录

    redis_client.lpush(recommend_user_key, video_id)

    # 如果达到了十个，就清空,并返回全部数据给推荐系统
    if redis_client.llen(recommend_user_key) >= 10:
        video_ids = redis_client.lrange(recommend_user_key, 0, -1)
        # 留空
        redis_client.delete(recommend_user_key)

    return exist(name, 1)


def get_sort(sort):
    '''
    获取分类视频具体实现
    '''
    result = get_values(sort, "sort", "video")
    # 理论上应该按热度排序
    # result.sort(reverse = True ,key = hot)
    t = []
    if result:
        # 排序完后提取
        for i in range(min(len(result), 50)):
            t .append(result[i].video_url)
    return result
