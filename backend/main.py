from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ws import sio
import socketio

api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@api.get("/hello")
async def root():
    return {"message": "Hello World"}


@api.get('/')
async def index():
    return {'result': 'success'}

app = socketio.ASGIApp(sio, api)
