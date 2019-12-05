# -*- coding:utf-8 -*-
__author__ = '_chao'


class RedisList(object):
    
    def __init__(self, client = None, **kwargs):
        self.r = client

    def get(self, key, *args, **kwargs):
        pass

    def update(self, key, *args):
        pass

    def delete(self, key, *args):
        pass

    def put(self, key, *args, **kwargs):
        pass


