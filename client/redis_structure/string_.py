# -*- coding:utf-8 -*-
__author__ = '_chao'


class RedisString(object):

    def __init__(self, client=None, **kwargs):
        self.r = client

    def get(self, key, *args, **kwargs):
        return self.r.get(key)

    def update(self, key, value, *args, **kwargs):
        self.r.set(key, value, xx=True)

    def delete(self, key, *args, **kwargs):
        self.r.delete(key)

    def exists(self, key):
        return self.r.get(key) is None

    def put(self, key, value, *args, **kwargs):
        self.r.set(key, value)

    def count(self, key):
        return self.r.strlen(key)
