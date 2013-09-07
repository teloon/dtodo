#!/usr/bin/env python
#-*- coding:utf-8 -*-

import pymongo
import tornado.web

from tornado.options import options

class CreateHandler(tornado.web.RequestHandler):

    def get(self):
        tid = self.create()
        self.redirect("/%s" % tid)

    def create(self):
        """
            create a new todo list page
            return: todo list id -- tid, string type
        """
        conn = pymongo.Connection(options.mongo_host, options.mongo_port)
        db = conn["main"]
        #get next seq
        cnter_coll = db["counters"]
        if not cnter_coll.find_one({"_id": "todo_lst"}):
            cnter_coll.insert({"_id": "todo_lst", "seq": 0})
        ret = cnter_coll.find_and_modify(
            query={"_id": "todo_lst"},
            update={"$inc": {"seq": 1}},
            new=True
        )
        seq = ret["seq"]
        #create todo list
        tid = self.gen_tid(seq)
        todos_coll = db["todo_lst"]
        todos_coll.insert({
            "tid": tid,
            "todos": [("hello world", "n"), ("book room", "y")],
        })
        return tid

    def gen_tid(self, num):
        """
            num: number, int type
            return: shorted url id, aka todo list id, string type
        """
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        BASE = len(alphabet)
        idx = 0
        c_lst = ["a"] * options.tid_len
        while num > 0:
            if idx >= options.tid_len:
                raise Exception("tid overflowed")
            c_lst[idx] = alphabet[num % BASE]
            idx += 1
            num /= BASE
        return "".join(c_lst)
