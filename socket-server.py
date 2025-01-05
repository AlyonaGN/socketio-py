import socketio
import eventlet
import eventlet.wsgi
from wsgiref.simple_server import make_server


sio = socketio.Server(cors_allowed_origins=[
        "http://localhost:5173",
        "http://localhost:3001"
    ])  

app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print(f"Client connected: {sid}")
    sio.emit("welcome", "Hello from Python Socket.IO!", to=sid)

@sio.event
def my_event(sid, data):
    print(f"Received my_event from {sid}: {data}")
    sio.emit("my_response", f"Got your message: {data}", to=sid)

@sio.event
def disconnect(sid):
    print(f"Client disconnected: {sid}")

if __name__ == "__main__":
    print("Serving Socket.IO on http://localhost:8080 ...")
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 8080)), app)
