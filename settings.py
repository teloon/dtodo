#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
import tornado.template

from tornado.options import define

ROOT = os.path.dirname(os.path.absname(__file__))

build_path = lambda *a: os.path.join(ROOT, *a)

define("port", default=8888, help="run on the given port", type=int)

MEDIA_ROOT = build_path(ROOT, 'media')
TEMPLATE_ROOT = build_path(ROOT, 'templates')

settings = {}
settings['static_path'] = MEDIA_ROOT
settings['template_loader'] = tornado.template.Loader(TEMPLATE_ROOT)
