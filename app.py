from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from threading import Thread, Event
from random import random


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index_page():
    return render_template('index.html')


@socketio.on('newdata')
def update_client_sensor_data():
    # Infinite loop to constantly update sensor data on client
    while True:
        emit('client', {'data': 'HELLO'})
        socketio.sleep(5)


@socketio.on('my event')
def test_message(message):
    emit('my response', {'data': message['data']})


@socketio.on('my broadcast event')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)


@socketio.on('connect')
def test_connect():
    print("Client connected")
    emit('newnumber', {'data': round(random() * 10, 3)})


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected.')


if __name__ == '__main__':
    socketio.run(app)
