# -*- coding:utf-8 -*-
__author__ = '_chao'

import redis
from client.redis_structure.manager import RedisTypeManager

class RedisClient(object):

    def __init__(self, name, host = None, port = None,
                 type = 'string', **kwargs):
        self.__init_client(host, port)
        self.type = type
        self.specific_client = RedisTypeManager(self.type, self.client).get_client()

    def __init_client(self, host, port):
        pool = self.get_connectionPool(host=host, port=port)
        self.client = redis.Redis(connection_pool=pool)

    def get_client(self):
        return self.client

    def get_connectionPool(self, host, port):
        '''
        获取连接池
        :param host:
        :param port:
        :return:
        '''
        return redis.ConnectionPool(host=host, port=port, decode_responses=True)

    def set_type(self, type):
        """
        设置类型（默认）
        :param type:
        :return:
        """
        self.specific_client = RedisTypeManager(type, self.client).get_client()

    def get(self, key, *args, **kwargs):
        return self.specific_client.get(key, *args, **kwargs)

    def update(self, key, value, *args, **kwargs):
        self.specific_client.update(key, value, *args, **kwargs)

    def put(self, key, value, *args, **kwargs):
        self.specific_client.put(key, value, *args, **kwargs)

    def delete(self, key, *args, **kwargs):
        self.specific_client.delete(key, *args, **kwargs)

    def exists(self, key):
        self.specific_client.exists(key)

    def count(self, key):
        return self.specific_client.count(key)

