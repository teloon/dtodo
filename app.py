#!/usr/bin/env python
#-*- coding:utf-8 -*-

import tornado.web
import tornado.httpserver
import tornado.ioloop

from settings import settings
from tornado.options import options
from urls import url_patt

class Application(tornado.web.Application):

    def __init__(self):
        tornado.web.Application.__init__(self, url_patt, **settings)

def test():
    app = Application()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    test()
