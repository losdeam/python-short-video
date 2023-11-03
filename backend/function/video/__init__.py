from .load import load 
from .qiniu import upload

def uploads(video,name):
    video_byte = load(video)
    return upload(name,video_byte)