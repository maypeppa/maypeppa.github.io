#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import logging
import time

from flask_socketio import SocketIO

DEFAULT_LOGGING_FORMAT = '[%(asctime)s][%(levelname)s]%(pathname)s@%(lineno)d: %(msg)s'
logging.basicConfig(level=logging.INFO, format=DEFAULT_LOGGING_FORMAT)
logger = logging.getLogger('trigger')

socketio = SocketIO(message_queue='redis://localhost/0', channel='socketio-test')
ns_name = '/fanout'
ts = int(time.time() * 1000)
socketio.emit('my event', ts, namespace=ns_name)
socketio.emit('my event', ts, namespace=ns_name)
socketio.emit('my event', ts, namespace=ns_name)
socketio.emit('my event', 'quit', namespace=ns_name)
