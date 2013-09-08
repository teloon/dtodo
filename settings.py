#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import tornado.template

from tornado.options import define

ROOT = os.path.dirname(os.path.abspath(__file__))

build_path = lambda *a: os.path.join(ROOT, *a)

define("port", default=8888, help="run on the given port", type=int)
define("mongo_host", default="localhost", help="server address of mongodb", type=str)
define("mongo_port", default=27017, help="port of mongodb server", type=int)
define("tid_len", default=5, help="the length of shorturl id ", type=int)

MEDIA_ROOT = build_path(ROOT, 'media')
TEMPLATE_ROOT = build_path(ROOT, 'templates')

settings = {}
settings['static_path'] = MEDIA_ROOT
settings['template_loader'] = tornado.template.Loader(TEMPLATE_ROOT)
settings['debug'] = True
