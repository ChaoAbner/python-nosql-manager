# -*- coding:utf-8 -*-
__author__ = '_chao'

class RedisString(object):

    def __init__(self, client=None, **kwargs):
        self.r = client

    def get(self, key):
        return self.r.get(key)

    def update(self, key, value):
        self.r.set(key, value, xx=True)

    def delete(self, key):
        self.r.delete(key)

    def put(self, key, value):
        self.r.set(key, value)

    def count(self, key):
        return self.r.strlen(key)
