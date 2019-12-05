# -*- coding:utf-8 -*-
__author__ = '_chao'

from config.config_getter import config

class ClientManager(object):
    def __init__(self):
        self.__init_client()


    def __init_client(self):
        __type =  config.db_type
        __mapper = config.client_mapper
        print(__type, __mapper)
        self.client = getattr(__import__(__type), __mapper)(name = config.db_name,
                                                host = config.db_host,
                                                port = config.db_port,
                                                password = config.db_passpord)

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

    def count(self):
        return self.client.count()


if __name__ == '__main__':
    c = ClientManager()
    c.put('proxy', 'dfd')
    print(c.get('proxy'))
    c.delete('proxy')
