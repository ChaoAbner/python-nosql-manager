# -*- coding:utf-8 -*-
__author__ = '_chao'

from config.config_getter import config


class ClientManager(object):

    def __init__(self):
        self.__init_clinet()


    def __init_clinet(self):
        __type =  config.db_type
        __mapper = config.client_mapper
        print(__type, __mapper)
        self.client = getattr(__import__(__type), __mapper)(name = config.db_name,
                                                host = config.db_host,
                                                port = config.db_port,
                                                password = config.db_passpord)
    def get(self, key, **kwargs):
        return self.client.get(key, **kwargs)

    def put(self, key, **kwargs):
        return self.client.put(key, **kwargs)

    def update(self, key, value, **kwargs):
        return self.client.update(key, value, **kwargs)

    def delete(self, key, **kwargs):
        return self.client.delete(key, **kwargs)

    def exists(self, key, **kwargs):
        return self.client.exists(key, **kwargs)

    def count(self):
        return self.client.count()


if __name__ == '__main__':
    c = ClientManager()
    table = c.client.set_table('hahaha')
    c.put({'proxy': '123.23.2.11'})
    print(c.count())