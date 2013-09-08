#!/usr/bin/env python
#-*- coding:utf-8 -*-

import re
import tornado.escape

def sanitize_text(s):
    new_s = tornado.escape.xhtml_unescape(s)
    new_s = re.sub(r"<div>", "\n", new_s)
    new_s = re.sub(r"</div>", "", new_s)
    return new_s
