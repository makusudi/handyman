# Handyman
Handyman is a simple event driven application based on Python (FastAPI), Celery, Redis and Vue.js.  It shows you how to 
integrate socket.io for any type of server and add "real-time effect" to your application.

Have fun :)

### Details
Project uses Socket.io as a transport protocol between backend, workers and client.  
All results and some temporary transport details stores in Redis.

### Running
    docker-compose build

    docker-compose up -d

    http://127.0.0.1:8080
