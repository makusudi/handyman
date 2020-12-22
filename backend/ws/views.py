import sys
import socketio
import random


sio = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins='*',
    allow_upgrades=True,
    logger=True,
    engineio_logger=True,
)


async def random_id(length):
    number = '0123456789'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    id = ''
    for i in range(0, length):
        id += random.choice(number)
        id += random.choice(alpha)
    return id


@sio.event
async def connect(sid, environ):
    print(f'Connected user with sid {sid}', file=sys.stdout, flush=True)


@sio.event
async def disconnect(sid):
    print(f'Client {sid} disconnected')


@sio.event
async def authenticate(sid, data):
    print(f'Trying to authenticate with credentials: {data}')
    await sio.emit('authenticate', {'authenticated': True}, to=sid)


@sio.event
async def create_task(sid, data):
    task_type = data.get('type')
    task_action = data.get('action')
    return await sio.emit('create_task', {'result': f'task type {task_type} with action {task_action}'})


@sio.event
async def get_result(sid, data):
    username = data.get('username')
    result = []
    for x in range(1, random.randint(6, 18)):
        res = {
            'username': username,
            'task_id': await random_id(5),
            'percent': random.randint(1, 100),
            'description': f'Description for task {x}',
            'priority': random.choice(['low', 'medium', 'high'])
        }
        result.append(res)

    return await sio.emit('get_result', result, to=sid)


@sio.event
async def info(sid, data):
    return await sio.emit('info', {'message': 'some information from server'})


