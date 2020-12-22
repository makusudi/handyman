import sys
import socketio

sio = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins='*',
    allow_upgrades=True,
    logger=True,
    engineio_logger=True
)


@sio.on('connect')
async def connect(sid, session):
    print(f'Connected user with sid {sid}', file=sys.stdout, flush=True)
    await sio.emit('custom_message', 'somedata', to=sid)


@sio.on('custom_message')
async def handle_trigger(sid, data):
    print(f'Received from: {sid}: {data}', file=sys.stdout, flush=True)
    return await sio.emit('custom_message', 'sdfsdfsdf')


@sio.on('disconnect')
async def disconnect(sid):
    print(f'Client {sid} disconnected')
