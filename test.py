from socketio import AsyncClient

scl = AsyncClient()


@scl.event
async def custom_message(data):
    print(f'I received {data}')


import asyncio


async def main():
    await scl.connect('ws://127.0.0.1:8000/io', socketio_path='/io/socket.io')
    print(scl.connection_url)
    print(scl.connected)
    print(scl.connection_namespaces)
    print(scl.connection_transports)
    await scl.emit('custom_message', 'DAATTTATAAAAAA')
    for _ in range(1, 10):
        await asyncio.sleep(0.3)
    print(f'disconnecting')
    await scl.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
