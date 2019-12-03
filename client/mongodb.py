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

    def get(self, filter = None, *args, **kwargs):
        return self.table.find_one(filter, *args, **kwargs)

    def update(self, spec, document):
        self.table.update(spec, document)

    def put(self, document):
        self.table.insert_one(document)

    def count(self):
        return self.table.count()

