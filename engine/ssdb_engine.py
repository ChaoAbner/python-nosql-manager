# -*- coding:utf-8 -*-
from client import ClientManager

__author__ = '_chao'



class SsDBEngine(ClientManager):
    def __init__(self):
        super().__init__('ssdb')