#!/usr/bin/env python
#-*- coding:utf-8 -*-

import tornado.web

class ListHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("list.html")
