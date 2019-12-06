# -*- coding:utf-8 -*-
__author__ = '_chao'

from os import getenv


# 默认数据库(此处修改默认数据库)
DEFAULT_DATABASE = "redis"

# 数据库配置（使用需修改）
DATABASE_COLLECTIONS = {
    "redis": {
        'TYPE': 'redis',
        'HOST': '127.0.0.1',
        'PORT': 6379,
        'PASSWORD': '',
        'NAME': ''
    },
    "mongodb": {
        'TYPE': 'mongodb',
        'HOST': '127.0.0.1',
        'PORT': 27017,
        'PASSWORD': '',
        'NAME': 'nosql_test'
    }
}

# 数据库配置
DATABASES = {
    "default": DATABASE_COLLECTIONS.get(DEFAULT_DATABASE)
}

# 定义宏
DB_TYPE = getenv('db_type', DATABASES.get('default').get('TYPE')).lower()
DB_HOST = getenv('db_host', DATABASES.get('default').get('HOST'))
DB_PORT = getenv('db_port', DATABASES.get('default').get('PORT'))
DB_NAME = getenv('db_name', DATABASES.get('default').get('NAME'))
DB_PASSWORD = getenv('db_password', DATABASES.get('default').get('PASSWORD'))

def change_db_configuration(type):
    if(type in DATABASE_COLLECTIONS.keys()):
        DATABASES['default'] = DATABASE_COLLECTIONS.get(type)
    else:
        raise ('Configuration of database does not exist')

# 数据库名与对应client的映射
MAPPER = {
    'CLIENT': {
        'redis': 'RedisClient',
        'mongodb': 'MongoDBClient',
        'ssdb': 'SsDBClient',
    },
    'STRUCTURE':{
        'redis': {
            'set': 'RedisSet',
            'list': 'RedisList',
            'string': 'RedisString',
            'hash': 'RedisHash',
        }
    }
}