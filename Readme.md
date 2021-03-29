# Handyman
Handyman is a simple event driven application based on Python, Celery, Redis and Vue.js.  It shows you how to 
integrate socket.io for any type of server and add "real-time effect" to your application.

By default backend runs with ASGI Socket.io server, but you can make some correction to
dockerfiles and run with Flask Socket.io server or FastAPI as well.  

Have fun :)

### Details
Project uses Socket.io as a transport protocol between backend, workers and client.  
All results and some temporary transport details stores in Redis.   
Dummy work provided by Celery worker is a string reversing. For example, if you call your task as "TASK", worker 
will return "KSAT" as a result of your task.

### Running
    docker-compose build

    docker-compose up -d

    http://127.0.0.1:8080
