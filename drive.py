from flask import Flask
import socketio
import eventlet

sio = socketio.Server()

app = Flask(__name__)

@sio.on('connect') #messgae, disconnect
def connect(sid, environ):
    print('connected')

if __name__ == '_main_':
    app = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('', 45676)), app)

