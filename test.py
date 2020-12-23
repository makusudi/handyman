from socketio import AsyncClient

scl = AsyncClient()


@scl.event
async def custom_message(data):
    print(f'I received {data}')


import asyncio


async def main():
    await scl.connect('ws://127.0.0.1:8000', namespaces=['tasks'])
    print(scl.connection_url)
    print(scl.connected)
    print(scl.connection_namespaces)
    print(scl.connection_transports)
    await scl.emit('custom_message', 'DAATTTATAAAAAA', namespace='tasks')
    for _ in range(1, 10):
        await asyncio.sleep(0.3)
    print(f'disconnecting')
    await scl.disconnect()

import aioredis

async def redis():
    redis = await aioredis.create_redis_pool('redis://127.0.0.1:6379/1')
    # await redis.set('my-key', '{redis: "redisss"}')
    # value = await redis.get('my-key', encoding='utf-8')
    # print(value)
    print(f'Channels = {redis.channels}')
    res: asyncio.Future = await redis.publish('/', 'HELLO')
    print(f'After publishing = {res}')
    for _ in range(10):
        print(res.done())
        await asyncio.sleep(0.5)
    while True:
        ch = await redis.keys('*')
        if ch:
            print(ch)
            break

    redis.close()


if __name__ == '__main__':
    asyncio.run(redis())
