# -*- coding:utf-8 -*-
__author__ = '_chao'


class RedisSet(object):

    def __init__(self, client=None, **kwargs):
        self.r = client

    def get(self, key, *args):
        return self.r.smembers(key)

    def update(self, key, *args):
        pass

    def delete(self, key, *args):
        self.r.srem(key, *args)

    def put(self, key, *args):
        self.r.sadd(key, *args)

    def count(self, key):
        return self.r.scard(key)

    def exists(self, key, member):
        return self.r.sismember(key, member)


