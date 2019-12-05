# -*- coding:utf-8 -*-
__author__ = '_chao'


from config.config_getter import config
import importlib

class RedisTypeManager(object):

    def __init__(self, type, client = None, **kwargs):
        mapper = config.structure_mapper
        type_ = 'client.redis_structure.{}_'.format(type)
        self.s = getattr(importlib.import_module(type_), mapper.get(type))(client = client)


    def get_client(self):
        return self.s
