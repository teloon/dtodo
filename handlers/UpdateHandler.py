#!/usr/bin/env python
#-*- coding:utf-8 -*-

import lib
import tornado.escape
import tornado.web
import pymongo

from tornado.options import options

class UpdateHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("OKKK!")

    def post(self):
        tid = self.get_argument("tid", "-1")
        td_idx = int(self.get_argument("td_idx"))
        new_todo = self.get_argument("new_todo")
        checked = self.get_argument("checked", "")
#        print "before:", new_todo.encode("utf-8")
        new_todo = tornado.escape.xhtml_escape(new_todo)
#        print "after:", new_todo.encode("utf-8")
        self.update_db(tid, td_idx, new_todo, checked)
        self.write("Successfully Update!")

    def update_db(self, tid, td_idx, new_todo, checked):
        conn = pymongo.Connection(options.mongo_host, options.mongo_port)
        db = conn["main"]
        coll = db["todo_lst"]
        doc = coll.find_one({"tid": tid})
        if len(doc["todos"]) == td_idx:
            if new_todo.strip() == "":
                return
            else:
                doc["todos"].append([new_todo, checked])
        elif new_todo.strip() == "":
            del doc["todos"][td_idx]
        else:
            doc["todos"][td_idx][0] = new_todo
            if checked == "y" or checked == "n":
                doc["todos"][td_idx][1] = checked
        coll.save(doc)
