# -*- coding:utf-8 -*-
__author__ = '_chao'

from os import getenv


# 默认数据库配置
DEFAULT_DATABASE = "redis"

DATABASE_COLLECTIONS = {
    "redis": {
        'db': 'redis_',
        'host': '127.0.0.1',
        'port': 6379,
        'password': '',
        'name': ''
    },
    "mongodb": {
        'db': 'mongodb',
        'host': '127.0.0.1',
        'port': 27017,
        'password': '',
        'name': 'nosql_test'
    }
}

# 定义宏
DB_TYPE = getenv('db_type', DATABASE_COLLECTIONS.get(DEFAULT_DATABASE).get('db')).lower()
DB_HOST = getenv('db_host', DATABASE_COLLECTIONS.get(DEFAULT_DATABASE).get('host'))
DB_PORT = getenv('db_port', DATABASE_COLLECTIONS.get(DEFAULT_DATABASE).get('port'))
DB_NAME = getenv('db_name', DATABASE_COLLECTIONS.get(DEFAULT_DATABASE).get('name'))
DB_PASSWORD = getenv('db_password', DATABASE_COLLECTIONS.get(DEFAULT_DATABASE).get('password'))


# 数据库配置
DATABASES = {
    "default": {
        "TYPE": DB_TYPE,
        "HOST": DB_HOST,
        "PORT": DB_PORT,
        "NAME": DB_NAME,
        "PASSWORD": DB_PASSWORD
    }
}

# 数据库名与对应client的映射
MAPPER = {
    'CLIENT': {
        'redis_': 'RedisClient',
        'mongodb': 'MongoDBClient',
        'ssdb': 'SsDBClient',
    },
    'STRUCTURE':{
        'redis_': {
            'set': 'RedisSet',
            'list': 'RedisList',
            'string': 'RedisString',
            'hash': 'RedisHash',
        }
    }
}