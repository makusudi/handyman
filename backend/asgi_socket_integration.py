import json
import random
import sys
import aioredis
import socketio
import uvicorn

from workers.asgi_socket_workers import some_work


manager = socketio.AsyncRedisManager('redis://redis_host:6379/0')
sio = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins='*',
    allow_upgrades=True,
    logger=True,
    engineio_logger=True,
    client_manager=manager,
)
app = socketio.ASGIApp(sio)


async def random_id(length: int) -> str:
    number = '0123456789'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    id = ''
    for i in range(0, length):
        id += random.choice(number)
        id += random.choice(alpha)
    return id


@sio.event
async def connect(sid: str, environ: str) -> None:
    print(f'Connected user with sid {sid}', file=sys.stdout, flush=True)
    sio.enter_room(sid, 'admin')


@sio.event
async def test(sid: str, message: dict) -> None:
    await sio.emit('test', {'test': 'success!'}, room='admin')


@sio.event
async def disconnect(sid: str) -> None:
    print(f'Client {sid} disconnected')


@sio.event
async def authenticate(sid: str, data: dict) -> None:
    print(f'Trying to authenticate with credentials: {data}')
    await sio.emit('authenticate', {'authenticated': True}, to=sid)


@sio.event
async def create_task(sid: str, data: dict) -> None:
    new: dict = {
        'task_id': await random_id(6),
        'description': data.get('description'),
        'username': 'admin',
        'percent': 0,
        'time': data.get('time'),
        'priority': data.get('priority'),
        'sid': sid,
        'result': None,
        'ready': False
    }
    some_work.apply_async(args=[new])
    await sio.manager.emit('create_task', new, to=sid)


@sio.event
async def get_result(sid: str, data: dict):
    result = []
    redis = await aioredis.create_redis_pool('redis://redis_host:6379/1')
    keys = await redis.keys('*')
    if keys:
        result = [json.loads(await redis.get(key)) for key in keys]

    return await sio.emit('get_result', result, to=sid)


if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=8000)
