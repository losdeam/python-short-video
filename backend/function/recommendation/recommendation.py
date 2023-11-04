

from surprise import accuracy, dump, SVD
from surprise.model_selection import KFold
from .data_processing import dataread
import os


# 检验模型是否存在（冷启动判断）
def model_exist(id):
    if id + '_model' in os.listdir("backend/model"):
        return True
    return False

# 为用户推荐tag


def recommend_tag(user):
    pass

# 在获取对应tag的视频列表后根据svd来预测，最高值则为推荐视频


def recommend_video(user):
    id = user['id']
    if model_exist(id):
        algo = dump.load("backend/model" + id + '_model')
        uid = str(196)
        iid = map(str, list(range(200)))
        for i in iid:
            pred = algo.predict(uid, i)
            print(pred)
    else:
        return recommend_cold()
    # 输出uid对iid的预测结果
    print(type(pred))

# 在用户视频栈满后，对用户的推荐模型进行更新


def recommend_update(user):
    data = dataread()
    id = user['id']
    if model_exist(id):
        algo = dump.load("backend/model" + id + '_model')
    else:
        algo = SVD()
    # ALS优化
    bsl_options = {'method': 'als', 'n_epochs': 5, 'reg_u': 12, 'reg_i': 5}
    kf = KFold(n_splits=3)
    for trainset, testset in kf.split(data):
        # 训练并预测
        algo.fit(trainset)
        predictions = algo.test(testset)
        # 计算RMSE
        accuracy.rmse(predictions, verbose=True)
    dump.dump('./svd_model', algo=algo)


# 用户冷启动
def recommend_cold():
    # 获取热门度最高的且未看过的视频
    pass


# 由外部调用的功能整合
def recommend(user):
    pass


hotness_weight = 0.45
# 结合热度进行打分


def score_with_hotness(ratings, video_hotness):
    scores = []
    for video_id, rating in ratings:
        hotness = video_hotness[video_id]
        score = hotness_weight * hotness + rating
        scores.append((video_id, score))
    return scores


def test():
    return os.listdir("backend/model")
