from surprise import Dataset
from surprise import Reader
import pandas as pd
from function.operate import user_like_history
from function.sql import get_value
def dataread(user_id):
    data,code = user_like_history(user_id)
    n  = len(data)
    # dict_ = {"user":[user_id for _ in range(n)],"item" : [],"rating":[],"timestamp":[i for i in range(n)]}
    dict_ = {"user":[user_id for _ in range(n)],"item" : [],"rating":[]}
    if code == 404 :
        return 404

    # 为所有种类的视频都添加相同数量的不点赞的记录，得分记录为0
    for type in ("游戏","动漫","科技","热点",'娱乐'):
        for index in range(1):
            dict_["user"].append(user_id)
            dict_["item"].append(type)
            dict_["rating"].append(0)
    # print("tttttttttt")
    # print(data)
    # 查询点赞队列中最近的十个视频，得分记录为1 
    for i in data :
        value = get_value(i,"video_id","video")
        if not value :
            print("视频丢失")
            continue 
        dict_["item"].append(value.sort)
        dict_["rating"].append(1)
    # print(dict_)
    df = pd.DataFrame(dict_)
    print(111111,df)

    reader = Reader(rating_scale=(1, 5)) 
  # data = Dataset.load_from_file('./ratings.csv', reader=reader)
    # print(222222,reader)
    data = Dataset.load_from_df(df,reader)
    print(1)
    print(data)
    return 200 