from fastapi import FastAPI
from asgi_socket_integration import app
import uvicorn


fastapi_app = FastAPI()


@fastapi_app.get('/healthcheck')
async def healthcheck() -> dict:
    return {'status': 'healthy'}


# here you can add specific routes depending on the app logic
fastapi_app.mount('/', app)


if __name__ == '__main__':
    uvicorn.run(app=fastapi_app, host='0.0.0.0', port=8000)
