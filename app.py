

from flask import Flask, render_template
from flask_socketio import SocketIO
import time 
import json 

from video_sent import Video_sent
app=Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('test.html')

# 当连接完毕则读取视频信息
@socketio.on('connect') 
def connect():
    global Video
    # print('Client connected') # s 在连接成功后发送消息
    Video = Video_sent("client","1.mp4")
    
@app.route('/test')
def test():
    #持续从视频流中获取帧信息
    n = 0
    while True:
        # print("传输进行中",n)
        # 通过Video_sent来获取本机的视频流数据
        frame=Video.get_frame()
        audio,n= Video.get_audio(n)
        datas =  {
            'time' : time.time(),
            'frame' : frame,
            'audio' : str(audio)
        }
        datas = json.dumps(datas)
        socketio.emit("play",datas)  
        time.sleep(1)

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=5003)
    socketio.run(app)