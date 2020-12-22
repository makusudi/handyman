from ws import sio
import socketio

app = socketio.ASGIApp(sio)
