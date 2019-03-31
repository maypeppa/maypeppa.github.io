#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import logging

from flask_socketio import SocketIO

DEFAULT_LOGGING_FORMAT = '[%(asctime)s][%(levelname)s]%(pathname)s@%(lineno)d: %(msg)s'
logging.basicConfig(level=logging.INFO, format=DEFAULT_LOGGING_FORMAT)
logger = logging.getLogger('trigger')

socketio = SocketIO(message_queue='redis://localhost/0', channel='flask-socketio')
socketio.emit('my event', 'hello world', namespace='/fanout')
socketio.send('raw message', namespace='/fanout')
