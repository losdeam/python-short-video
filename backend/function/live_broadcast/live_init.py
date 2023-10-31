from flask_socketio import SocketIO,join_room, leave_room
from .live_push import push

#以字典的形式保存已有直播间，格式为 {房间号：[观众id_1,观众id_2,...]}
live_room = {}
flag_live = True 
# 开播
def create(data):
    global flag_live
    room = data["room"]
    if room in live_room :
        return "您的直播间已开启，请不要重复打开直播间"
    join_room(room)
    live_room[room] = set()

# 下播
def close(data,socket):
    global flag_live
    flag_live = False 
    socket.emit('stop')
    leave_room(data["room"])
    # 停止推送，

# 观众部分
# 进入直播间
def join(user):
    room = user["room"]
    if room not in live_room :
        return "主播还没开播"
    join_room(room)
    live_room[room].add(user['id'])

# 退出直播间
def leave(user):
    room = user["room"]
    leave_room(room)
    live_room[room].discard(user['id'])

