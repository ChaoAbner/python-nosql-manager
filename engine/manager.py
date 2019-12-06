# -*- coding:utf-8 -*-
__author__ = '_chao'

from engine.mongodb_engine import MongoDBEngine
from engine.redis_engine import RedisEngine
from engine.ssdb_engine import SsDBEngine

class Engine(object):

    @property
    def mongodb(self):
        return MongoDBEngine()

    @property
    def redis(self):
        return RedisEngine()

    @property
    def ssdb(self):
        return SsDBEngine()