# -*- coding:utf-8 -*-
__author__ = '_chao'

from os import getenv


# 默认数据库配置
DEFAULT_DATABASE = {
    # 'db': 'redis',
    'db': 'mongodb',
    'host': '127.0.0.1',
    # 'port': 6379,
    'port': 27017,
    'name': 'nosql_test',
    'password': ''
}

# 定义宏
DB_TYPE = getenv('db_type', DEFAULT_DATABASE.get('db')).lower()
DB_HOST = getenv('db_host', DEFAULT_DATABASE.get('host'))
DB_PORT = getenv('db_port', DEFAULT_DATABASE.get('port'))
DB_NAME = getenv('db_name', DEFAULT_DATABASE.get('name'))
DB_PASSWORD = getenv('db_password', DEFAULT_DATABASE.get('password'))

# 数据库名与对应client的映射
DATABASE_CLIENT_MAPPER = {
    'redis': 'RedisClient',
    'mongodb': 'MongoDBClient',
    'ssdb': 'SsDBClient',
}


""" 数据库配置 """
DATABASES = {
    "default": {
        "TYPE": DB_TYPE,
        "HOST": DB_HOST,
        "PORT": DB_PORT,
        "NAME": DB_NAME,
        "PASSWORD": DB_PASSWORD
    }
}