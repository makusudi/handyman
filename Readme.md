# Handyman
Handyman is a simple event driven application based on Python, Celery, Redis and Vue.js.  It shows you how to 
integrate socket.io for any type of server and add "real-time effect" to your application.

By default backend runs with Flask and Socket.io, but you can make some correction to
docker-compose and run with ASGI Socket.io Server or FastAPI as well.  

Have fun :)

### Details
Project uses Socket.io as a transport protocol between backend, workers and client.  
All results and some temporary transport details stores in Redis.

### Running
    docker-compose up -d

    http://127.0.0.1:8080
