from os import getenv
import socketio

# standard Python
sio = socketio.Client()

server_url = getenv('SERVER_URL') or "http://localhost:1337"
sio.connect(server_url)

@sio.on('connect')
def on_connect():
    sio.emit('joinLaunchTimer')
    print('connected')


@sio.on('disconnect')
def on_disconnect():
    print("g'bye")
