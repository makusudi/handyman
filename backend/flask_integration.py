import random
import sys
import eventlet
from flask import Flask, session
from flask_socketio import SocketIO, emit, join_room
import logging
import uuid
import json
import redis
from workers.flask_workers import some_work

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

eventlet.monkey_patch()

server = Flask(__name__)

sio = SocketIO(
    server,
    mode='eventlet',
    message_queue='redis://redis_host:6379/0',
    cors_allowed_origins='*'
)


def random_id(length: int) -> str:
    number = '0123456789'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    id = ''
    for i in range(0, length):
        id += random.choice(number)
        id += random.choice(alpha)
    return id


@sio.on('connect')
def connect() -> None:
    session['uid'] = session.get('uid') or str(uuid.uuid4())
    # join_room(session['uid'])
    join_room('admin')
    print(f'Connected user with sid {session["uid"]}', file=sys.stdout, flush=True)


@sio.on('disconnect')
def disconnect(data: dict) -> None:
    print(f'Client {data} disconnected')


@sio.on('authenticate')
def authenticate(data: dict) -> None:
    print(f'Trying to authenticate with credentials: {data}')
    emit('authenticate', {'authenticated': True})


@sio.on('create_task')
def create_task(data: dict) -> None:
    print(session)
    new: dict = {
        'task_id': random_id(6),
        'description': data.get('description'),
        'username': 'admin',
        'percent': 0,
        'time': data.get('time'),
        'priority': data.get('priority'),
        'sid': session.get('uid'),
        'result': None,
        'ready': False
    }
    some_work.apply_async(args=[new])
    emit('create_task', new)


@sio.on('get_result')
def get_result(data: dict) -> None:
    result = []
    connection = redis.Redis(host='redis_host', port=6379, db=1)
    keys = connection.keys('*')
    if keys:
        result = [json.loads(connection.get(key)) for key in keys]
    emit('get_result', result)


if __name__ == '__main__':
    sio.run(server, host='0.0.0.0', port=8000, debug=True)
