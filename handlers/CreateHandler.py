#!/usr/bin/env python
#-*- coding:utf-8 -*-

import tornado.web

class CreateHandler(tornado.web.RequestHandler):

    def get(self):
        tid = self.gen_tid()
        self.redirect("/%s" % tid)

    def gen_tid(self):
        """
            generate todo list id
        """
        return "abc12"
