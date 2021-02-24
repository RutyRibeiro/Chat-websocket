from flask import Flask
from flask_socketio import SocketIO, send

# Use socketio = SocketIO(app, cors_allowed_origins='*')   to remove cors error 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('message')
def handleMessage(msg):
    print(f'Message: {msg}')
    send(msg, broadcast= True)

if __name__ == '__main__':
    socketio.run(app)
