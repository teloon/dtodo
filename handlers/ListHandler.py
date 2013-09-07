#!/usr/bin/env python
#-*- coding:utf-8 -*-

import tornado.web
import pymongo

from tornado.options import options

class ListHandler(tornado.web.RequestHandler):

    def get(self, tid):
        todos = self.get_todos(tid)
        self.render("list.html", tid=tid, todos=todos)

    def get_todos(self, tid):
        conn = pymongo.Connection(options.mongo_host, options.mongo_port)
        db = conn["main"]
        todos_coll = db["todo_lst"]
        doc = todos_coll.find_one({"tid": tid})
        return doc["todos"]
