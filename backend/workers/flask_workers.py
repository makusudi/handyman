from celery import Celery
from celery.signals import task_postrun
import time
import sys
import json
from flask_socketio import SocketIO
import redis


application = Celery('CeleryAppName', broker='redis://redis_host:6379/0')
application.conf.backend = 'redis://redis_host:6379/0'
application.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='Europe/Moscow',
    enable_utc=True,
)


@application.task(bind=True, name='creator')
def some_work(self, some_data: dict) -> dict:
    res = some_data
    connection = redis.Redis(host='redis_host', port=6379, db=1)
    sock = SocketIO(message_queue='redis://redis_host:6379/0')
    print(f'Sleeping for {res.get("time")}', file=sys.stdout, flush=True)
    for x in range(int(res.get('time') / 2)):
        res['percent'] = res.get('percent') + (100 / (int(res.get('time') / 2)))
        print(f'Emitting message')
        sock.emit('worker_message', res, room='admin')
        connection.set(res.get('task_id'), json.dumps(res))
        time.sleep(2)
    return res


@task_postrun.connect()
def task_postrun(retval=None, task_id=None, task=None, args=None, **kwargs):
    print(f'Finishing with task {task}')
    connection = redis.Redis(host='redis_host', port=6379, db=1)
    retval['percent'] = 100
    retval['ready'] = True
    retval['result'] = retval['description'][::-1]
    connection.set(retval.get('task_id'), json.dumps(retval))
    sock = SocketIO(message_queue='redis://redis_host:6379/0')
    print(f'Redis has been updated')
    sock.emit('worker_message', retval, room='admin')
    print(f'User has been informed')
