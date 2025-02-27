from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
sock = SocketIO(app)

@app.route('/')
def hello():
    return 'I am gRoot'

@app.route('/index')
def index():
    return render_template('index.html')


@sock.on('connect')
def conn():
    print('a client connected')

@sock.on('message')
def mess(d):
    print(f'received a message: {d}')
    sock.emit('response',f'Server received the message: {d}')

if __name__ == '__main__':
    sock.run(app,debug=True)