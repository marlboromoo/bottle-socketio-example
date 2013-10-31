#!/usr/bin/env python
# encoding: utf-8

import bottle
from bottle.ext import redis
from redis import Redis
from socketio import socketio_manage
from socketio.namespace import BaseNamespace
from gevent import monkey

monkey.patch_all()
app = bottle.Bottle()
plugin = redis.RedisPlugin()
app.install(plugin)

def get_redis_from_app(app):
    attr = 'redisdb'
    for p in app.plugins:
        if hasattr(p, attr):
            return Redis(connection_pool=getattr(p, attr))
    return None

class TestNamespace(BaseNamespace):
    def on_join(self, msg):
        redis = get_redis_from_app(app)
        key = channel = 'foo'
        self.emit('recive', msg)
        sub = redis.pubsub()
        sub.subscribe(channel)
        for i in sub.listen():
            if i['type'] == 'message':
                self.emit('recive', redis.lrange(key, -1, -1))
        sub.unsubscribe()

@app.get('/')
def root():
    return bottle.template('index')

@app.get('/_static/<filepath:path>')
def get_static(filepath):
    return bottle.static_file(filepath, root='./static/')

@app.get('/socket.io/<path:path>')
def socketio_service(path):
    socketio_manage(bottle.request.environ,
                    {'/test': TestNamespace}, bottle.request)

if __name__ == '__main__':
    bottle.run(app=app,
               host='127.0.1.1',
               port=8080,
               server='geventSocketIO',
               debug=True,
               reloader=True,
              )
