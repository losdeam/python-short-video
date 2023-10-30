
import utils.function as function 

from moviepy.editor import VideoFileClip

class Video_load:

    def __init__(self,name="w1",capture=1):
        # 初始化
        self.name = name
        self.video = VideoFileClip(capture)  
        # 获取音频时长以确定视频的总时长
        self.video_time = self.video.duration

        audio= self.video.audio
        # 将音频信息暂存为wav文件方便进行读取
        audio.write_audiofile(self.name + '.wav')

        


        

