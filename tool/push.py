#!/usr/bin/env python
# encoding: utf-8

import redis
import random

pool = redis.ConnectionPool(host='127.0.0.1')
db = redis.Redis(connection_pool=pool)

key = channel = 'foo'
db.rpush(key, random.randint(1, 1000))
db.publish(channel, True)
print db.lrange(key, -1, -1)


