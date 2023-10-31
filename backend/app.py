# 跨域
from flaskr import create_app



if __name__=="__main__":
    app,socketio = create_app()
    app.run(debug=True, host = "0.0.0.0",port=50000)
    socketio.run(app)
