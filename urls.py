#!/usr/bin/env python
#-*- coding:utf-8 -*-

from handlers.IndexHandler import IndexHandler
from handlers.CreateHandler import CreateHandler
from handlers.ListHandler import ListHandler

url_patt = [
    (r"/", IndexHandler),
    (r"/create", CreateHandler),
    (r"/[a-zA-Z0-9]{5}", ListHandler),
]
