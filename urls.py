#!/usr/bin/env python
#-*- coding:utf-8 -*-

from tornado.options import options

from handlers.IndexHandler import IndexHandler
from handlers.CreateHandler import CreateHandler
from handlers.ListHandler import ListHandler
from handlers.UpdateHandler import UpdateHandler

url_patt = [
    (r"/", IndexHandler),
    (r"/create", CreateHandler),
    (r"/update", UpdateHandler),
    (r"/([a-zA-Z0-9]{%s})" % options.tid_len, ListHandler),
]
