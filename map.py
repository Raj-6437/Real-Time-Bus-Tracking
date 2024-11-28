from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

user_locations = []

@app.route('/')
def index():
    return "Real-Time Location Backend"

@socketio.on('send_location')
def handle_location(data):
    global user_locations
    user_exists = False

    # Update location if user already exists
    for user in user_locations:
        if user['id'] == data['id']:
            user['lat'] = data['lat']
            user['lng'] = data['lng']
            user_exists = True
            break

    # Add new user if not found
    if not user_exists:
        user_locations.append(data)

    emit('update_location', user_locations, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
