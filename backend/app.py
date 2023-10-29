# 跨域
from flask_cors import CORS

from flask import Flask, render_template
from flask_socketio import SocketIO
from utils.function import call
from utils.video_load import Video_load
from utils.video_sent import Video_sent
import requests as request
import time 
import json 




app=Flask(__name__)
socketio = SocketIO(app)

# 跨域
CORS(app, supports_credentials=True)

# 设置SESSION_COOKIE_SAMESITE为 'None'，确保支持跨站点 Cookie
# app.config['SESSION_COOKIE_SAMESITE'] = 'None'

# 设置SESSION_COOKIE_SECURE为 'True'，要求使用安全的 HTTPS 连接
# app.config['SESSION_COOKIE_SECURE'] = True



# 当连接完毕
@socketio.on('connect') 
def connect():
    global connected
    connected = True 
    print('已成功连接')

# 当连接完毕,收到test信号时
@socketio.on('test') 
def test():
    print('已成功连接')
    global Video_loads
    video_name = "1.mp4"
    Video_loads = Video_load("client",video_name)
    datas = {
        "msg" : f"video {video_name} load  finish", 
        "time": Video_loads.video_time
    }
    datas = json.dumps(datas)
    socketio.emit("read",datas)  
    print("视频读取完毕")

    print("开始发送")
    video = Video_sent(Video_loads)
    #持续从视频流中获取帧信息
    n = 0
    # 当连接时，持续发送
    while connected:
        # print("传输进行中",n)
        # 通过Video_sent来获取本机的视频流数据
        frame=video.get_frame()
        audio,n= video.get_audio(n)
        # print(type(frame),type(audio))
        if not (frame or   audio):
            break
        datas =  {
            'time' : time.time(),
            'frame' : frame,
            'audio' : str(audio)
        }
        datas = json.dumps(datas)
        socketio.emit('play',datas)  
    print("发送完毕")
    socketio.emit('sent_finish')  

# 当连接完毕,收到read信号时
@socketio.on('read') 
def read():
    print('已成功连接')
    global Video_loads
    video_name = "1.mp4"
    Video_loads = Video_load("client",video_name)
    datas = {
        "msg" : f"video {video_name} load  finish", 
        "time": Video_loads.video_time
    }
    datas = json.dumps(datas)
    socketio.emit("read",datas)  
    print("视频读取完毕")
    
# 当连接完毕,收到sent_start信号时
@socketio.on('sent_start') 
def sent():
    print("开始发送")
    video = Video_sent(Video_loads)
    #持续从视频流中获取帧信息
    n = 0
    # 当连接时，持续发送
    while connected:
        # print("传输进行中",n)
        # 通过Video_sent来获取本机的视频流数据
        frame=video.get_frame()
        audio,n= video.get_audio(n)
        # print(type(frame),type(audio))
        if not (frame or   audio):
            break
        datas =  {
            'time' : time.time(),
            'frame' : frame,
            'audio' : str(audio)
        }
        datas = json.dumps(datas)
        socketio.emit('play',datas)  
    print("发送完毕")
    socketio.emit('sent_finish')  

@socketio.on('disconnect') 
def disconnect ():
    global connected
    connected = False 

# 
@app.route('/')
def index():
    return render_template('index.html')

# 当访问read页面时，进行读取（后续应修改为post请求）
# 本质上是后端的读取，所以只需要进行一次
@app.route('/read')
def  read ():
    return render_template('read.html')

# 当访问play页面时，进行播放（后续应修改为post请求） 
# 每次访问都需要重复进行，后续应获取客户端已经收到的最高帧数，实现断连后继续传输的效果而不是每次都从头传输
@app.route('/play')
def play():
    return render_template('play.html')


# 当访问read页面时，进行读取（后续应修改为post请求） 
@app.route('/test')
def test():
    return render_template('test.html')


# 接口
@app.route('/emit', methods=['POST']) 
def emit_event():
    print('已成功连接')
    global Video_loads
    video_name = "1.mp4"
    Video_loads = Video_load("client",video_name)
    datas = {
        "msg" : f"video {video_name} load  finish", 
        "time": Video_loads.video_time
    }
    datas = json.dumps(datas)
    socketio.emit("read",datas)  
    print("视频读取完毕")

    print("开始发送")
    video = Video_sent(Video_loads)
    #持续从视频流中获取帧信息
    n = 0
    # 当连接时，持续发送
    while connected:
        # print("传输进行中",n)
        # 通过Video_sent来获取本机的视频流数据
        frame=video.get_frame()
        audio,n= video.get_audio(n)
        # print(type(frame),type(audio))
        if not (frame or   audio):
            break
        datas =  {
            'time' : time.time(),
            'frame' : frame,
            'audio' : str(audio)
        }
        datas = json.dumps(datas)
        socketio.emit('play',datas)  
    print("发送完毕")
    socketio.emit('sent_finish')  

if __name__=="__main__":
    app.run(debug=False, host = "0.0.0.0",port=50000)
    socketio.run(app)
