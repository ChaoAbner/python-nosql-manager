# -*- coding:utf-8 -*-
__author__ = '_chao'

from pymongo import MongoClient

class MongoDBClient(object):

    def __init__(self, name, host = None, port = None, **kwargs):
        self.client = MongoClient(host, port, **kwargs)
        self.db = self.client[name]

    def set_table(self, table_name):
        self.table = self.db[table_name]
        return self.db[table_name]

    def get_client(self):
        return self.client

    def get(self, filter = None, *args, **kwargs):
        return self.table.find_one(filter, *args, **kwargs)

    def update(self, spec, document, *args, **kwargs):
        self.table.update(spec, document, *args, **kwargs)

    def put(self, document, *args, **kwargs):
        self.table.insert_one(document, *args, **kwargs)

    def delete(self, filter, *args, **kwargs):
        self.table.delete_one(filter, *args, **kwargs)

    def count(self):
        return self.table.count()

