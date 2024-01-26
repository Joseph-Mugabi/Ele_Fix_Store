+6from flask import Flask, render_template
from flask_socketio import SocketIO, send
import secrets
from models import storage
from models.users import User
from flask_login import current_user

app = Flask(__name__)

app.config['SECRET_KEY'] = secrets.token_hex(32)
socketio = SocketIO(app, cors_allowed_origins="*")
app.debug = True

@app.route('/chat')
def index():
    """assuming you are using flsk logn to manage usr sessions"""
    user = current_user
    return render_template('messaging.html', user=user)

@socketio.on('message')
def handle_message(data):
    print('Received message: ' + data)
    if data != "I\'m connected!":
        send(data, broadcast=True)
    #socketio.emit('message', data, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5002)
