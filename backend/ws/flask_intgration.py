import random
import sys
import eventlet
from flask import Flask, session
from flask_socketio import SocketIO, emit, join_room
import logging
import uuid

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

eventlet.monkey_patch()

server = Flask(__name__)
sio = SocketIO(server, mode='eventlet', message_queue='redis://localhost:6379/0', cors_allowed_origins='*')


def random_id(length):
    number = '0123456789'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    id = ''
    for i in range(0, length):
        id += random.choice(number)
        id += random.choice(alpha)
    return id


@sio.on('connect')
def connect():
    session['uid'] = session.get('uid') or str(uuid.uuid4())
    join_room(session['uid'])
    print(f'Connected user with sid {session["uid"]}', file=sys.stdout, flush=True)


@sio.on('disconnect')
def disconnect(data):
    print(f'Client {data} disconnected')


@sio.on('authenticate')
def authenticate(data):
    print(f'Trying to authenticate with credentials: {data}')
    emit('authenticate', {'authenticated': True})


@sio.on('create_task')
def create_task(data: dict):
    new: dict = {
        'task_id': random_id(6),
        'description': data.get('description'),
        'username': 'admin',
        'percent': 0,
        'time': data.get('time'),
        'priority': data.get('priority')
    }
    # await sio.manager.emit('create_task', new, to=sid)
    emit('create_task', new)
    # await sio.emit('create_task', new, to=sid)


@sio.on('get_result')
def get_result(data):
    username = data.get('username')
    result = []
    for x in range(1, random.randint(6, 18)):
        res = {
            'username': username,
            'task_id': random_id(5),
            'percent': random.randint(1, 100),
            'description': f'Description for task {x}',
            'priority': random.choice(['low', 'medium', 'high'])
        }
        result.append(res)

    return emit('get_result', result)


@sio.on('info')
def info(data):
    return emit('info', {'message': 'some information from server'})


if __name__ == '__main__':
    sio.run(server, host='0.0.0.0', port=8000, debug=True)
