# -*- coding:utf-8 -*-

from config import setting

__author__ = '_chao'


class ConfigGetter(object):

    def __init__(self):
        pass

    @property
    def db_type(self):
        return setting.DATABASES.get("default", {}).get('TYPE')

    @property
    def db_host(self):
        return setting.DATABASES.get("default", {}).get('HOST')

    @property
    def db_port(self):
        return setting.DATABASES.get("default", {}).get('PORT')

    @property
    def db_name(self):
        return setting.DATABASES.get("default", {}).get('NAME')

    @property
    def db_passpord(self):
        return setting.DATABASES.get("default", {}).get('PASSWORD')

    @property
    def client_mapper(self):
        return setting.MAPPER.get('CLIENT').get(self.db_type)

    @property
    def structure_mapper(self):
        return setting.MAPPER.get('STRUCTURE').get(self.db_type)


config = ConfigGetter()