from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'myRealTimeAppSecretSalt'
socketio = SocketIO(app)

@app.route('/')
def home_page():
    return render_template('index.html'), 200

@socketio.on('on_data_update')
def handle_data_update(data):
    socketio.emit('on_data_update', data)

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5051)