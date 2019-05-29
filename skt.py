from os import getenv
import socketio
from time import sleep

# standard Python
sio = socketio.Client()
server_url = getenv('SERVER_URL') or "http://localhost:1337"

@sio.on('connect')
def on_connect():
    sio.emit('joinLaunchTimer')
    print('connected')


@sio.on('disconnect')
def on_disconnect():
    print("g'bye")


def connect(sio, server_url, sleepTime=5):
    print("connecting to server %s" % server_url)
    try:
        sio.connect(server_url)
    except:
        print("encountered error connecting. Retrying in %d seconds" % sleepTime)
        sleep(sleepTime)
        connect(sio, server_url, sleepTime*2)


connect(sio, server_url)
