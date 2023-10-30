from flask import Flask, render_template, url_for, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MyChatApplicationSecret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    name = request.args.get('name')
    return render_template('index.html', username=name)

@socketio.on('robinapp_message')
def handle_message(msg):
    socketio.emit('robinapp_message', msg)

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5051)