import cv2

import base64
import json
import function
import pyaudio
import wave 
from moviepy.editor import VideoFileClip

class Video_sent:

    def __init__(self,name="w1",capture=1):
        print (name)
        # 初始化
        self.name = name
        video = VideoFileClip(capture)  
        audio= video.audio
        self.video = video.iter_frames()
        
        audio.write_audiofile('sound.wav')
        self.wf = wave.open('sound.wav', 'rb')
        self.len = self.wf.getnframes()

    #图像转base64
    def get_frame(self):
        if self.video:
            img = next(self.video)
            # 图像预处理
            img = function.transform(img)
            #图像转base64
            img_bytes = cv2.imencode('.png', img)[1].tostring()
            img_str = base64.b64encode(img_bytes).decode('utf-8')
            
            return img_str
        return None
    
    #音频转base64
    def get_audio(self,n):

        if n < self.len:
            # 从上传的视频流中获取音频信息
            audio_data = self.wf.readframes(1024) 
            n+= len(audio_data)
            return audio_data ,n 
        return None ,n 
    


    def colse(self):
        # 如果存在已经开启的视频文件
        self.cam.release()
        if self.input_stream:
            self.input_stream.stop_stream()
            self.input_stream.close()
        self.p.terminate()
        
        

