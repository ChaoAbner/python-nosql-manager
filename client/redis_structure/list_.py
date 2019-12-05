# -*- coding:utf-8 -*-
__author__ = '_chao'


class RedisList(object):
    
    def __init__(self, client = None):
        self.r = client

    def get(self, key, *args, **kwargs):
        return self.r.lrange(key, args[0], args[1])

    def update(self, key, *args):
        self.r.lset(key, args[0], args[1])

    def delete(self, key, *args):
        self.r.lrem(key, args[0], args[1])

    def put(self, key, *args, **kwargs):
        self.r.lpush(key, *args)

    def count(self, key):
        return self.r.llen(key)
