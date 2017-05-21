#!/usr/bin/env python
# coding=utf-8
__author__ = 'larkin'

import tornado.web
import tornado.ioloop
import os

PORT = 6565
HANDLERS = [
    ('/(.*)', tornado.web.StaticFileHandler, {'path': os.path.dirname(__file__) + 'static'}),
    ]

if __name__ == "__main__":
    settings = {"static_path": os.path.join(os.path.dirname(__file__), "static")}
    app = tornado.web.Application(HANDLERS, **settings)
    app.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()
