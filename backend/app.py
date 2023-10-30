# 跨域
from flask_cors import CORS,request

from flask import Flask, render_template
from flask_socketio import SocketIO,join_room, leave_room
from utils.function import call
from function.video.video_load import Video_load
from function.video.video_sent import Video_sent
from function.video.video_upload import upload
from function.live_broadcast.live_create import live_create
from function.live_broadcast.live_push import live_push
import time 
import json 




app=Flask(__name__)
socketio = SocketIO(app)

# 跨域
CORS(app, supports_credentials=True)

# 当连接完毕
@socketio.on('connect') 
def connect():
    global connected
    connected = True 
    

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


# get 形式的测试接口
@app.route('/test_1')
def test_1():
    data = {
        "message" : "Hi.AirCode",
        "src" : "http://s360yyqhm.hn-bkt.clouddn.com/1.mp4"
    }
    return json.dumps(data)

@app.route('/token_get', methods=['POST'])
def token_get(data):
    return upload(data["name"])

@app.route('/live_create', methods=['POST'])
def live_create(data):
    room = data['room']
    join_room(room)

@app.route('/live_join', methods=['POST'])
def live_join(data):
    room = data['room']
    join_room(room)
    while connected:
        live_push(data['frame'])
    leave_room(room)
    
    


if __name__=="__main__":
    app.run(debug=False, host = "0.0.0.0",port=50000)
    socketio.run(app)
