
connect = True 
#视频推流
def push(data,socket):
    frame = data['frame']
    audio = data['audio']
    if connect :
        socket.emit('push',{"frame":frame,"audio":audio});

# 强制中断
def force_close(user): 
    if 1 : # 验证用户权限,若可行便执行
        global connect 
        connect = False 

# 管理员警告（用于制止不良行为）
def force_warning(user,socket):
    if 1 :
        socket.emit('waring');
    
    
    
    
