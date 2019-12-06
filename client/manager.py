# -*- coding:utf-8 -*-
__author__ = '_chao'

import importlib

from config.config_getter import config
from config.setting import change_db_configuration

class ClientManager(object):
    def __init__(self, db_type = None):
        self.__init_client(db_type)

    def __init_client(self, db_type):
        if db_type:
            __type = db_type.lower()
            change_db_configuration(db_type)
        else:
            __type = config.db_type
        __mapper = config.client_mapper(__type)
        __module_path = 'client.{}'.format(__type)
        self.client = getattr(importlib.import_module(__module_path), __mapper)(name = config.db_name,
                                                host = config.db_host,
                                                port = config.db_port,
                                                password = config.db_passpord)

    def change_db(self, db_type):
        db_type = db_type.lower()
        change_db_configuration(db_type)
        return self.__init_client(db_type)

    def get_client(self):
        return self.client.get_client()

    def get(self, key, *args, **kwargs):
        return self.client.get(key, *args, **kwargs)

    def put(self, key, value, *args, **kwargs):
        return self.client.put(key, value, *args, **kwargs)

    def update(self, key, value, *args, **kwargs):
        return self.client.update(key, value, *args, **kwargs)

    def delete(self, key, *args, **kwargs):
        return self.client.delete(key, *args, **kwargs)

    def exists(self, key, *args, **kwargs):
        return self.client.exists(key, *args, **kwargs)

    def count(self, key):
        return self.client.count(key)


if __name__ == '__main__':
    c = ClientManager()
    c.put('proxy', 'dfd')
    print(c.get('proxy'))

    # 切换redis的数据结构类型
    c.client.set_type('hash')
    c.put('hash', 'k1', 'v1')
    print(c.get('hash', 'k1'))

    c.client.set_type('list')
    # c.put('list', 1,2,3)
    print(c.get('list',0,-1))
    print(c.count('list'))

    c.client.set_type('set')
    c.put('set', 1,2,3,3)
    print(c.get('set'))
    print(c.count('set'))

    c.change_db('mongodb')
    mongo = c.get_client()
    mongo = mongo.nosql_test.hahaha
    res = mongo.find({'proxy': '123.23.2.11'})
    print(res)
