# -*- coding:utf-8 -*-
__author__ = '_chao'

from engine.manager import Engine

if __name__ == '__main__':
    # 使用MongoDB
    mongo = Engine().mongodb
    m_client = mongo.get_client()
    db = m_client.nosql_test
    coll = db.hahaha
    for i in coll.find():
        print(i)

    # 获得当前数据库
    db = mongo.db
    # 更换表
    db.set_table('hahaha')
    # 使用内置简单方法
    print(db.count())

    # 使用redis
    redis = Engine().redis
    r_client = redis.get_client()
    print(r_client.get('python'))

    # 使用简单内置方法
    redis.put('inner', '123hello')
    print(redis.get('inner'))


