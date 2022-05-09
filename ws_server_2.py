import time

from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit
app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')
# import main
url = 'https://beetaexch.com/casino/dt202'




@socketio.on('url')
def handle_message(data):
    url = data
    print("URL : ", url)


@socketio.on('play')
def handle_message(data):
    url = 'https://beetaexch.com/casino/dt202'
    # main.scrape(emit,url)
    file = "ss.mp4"
    f = open(file, 'rb')
    with open(file, 'rb') as f:
        # print(f.read())
        emit("video", f.read())


    # while True:
    #     time.sleep(2)
    #     piece = f.read(1024)
    #     print(piece)
    #     if not piece:
    #         break
    #     emit("video","video")
    # f.close()


if __name__ == '__main__':
    socketio.run(app, host="127.0.0.1", port=24212)
