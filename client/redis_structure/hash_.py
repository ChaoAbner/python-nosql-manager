# -*- coding:utf-8 -*-
__author__ = '_chao'


class RedisHash(object):
    
    def __init__(self, client = None, **kwargs):
        self.r = client

    def get(self, key, *args, **kwargs):
        return self.r.hget(key, args[0])

    def update(self, key, *args, **kwargs):
        self.r.hset(key, args[0], args[1])

    def delete(self, key, *args, **kwargs):
        self.r.hdel(key, args[0])

    def put(self, key, *args, **kwargs):
        self.r.hsetnx(key, args[0], args[1])

    def count(self, key):
        return self.r.hlen(key)
