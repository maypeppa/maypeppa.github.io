#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import logging

from socketIO_client import BaseNamespace, SocketIO

logger = logging.getLogger('client')
DEFAULT_LOGGING_FORMAT = '[%(asctime)s][%(levelname)s]%(filename)s@%(lineno)d: %(msg)s'
logging.basicConfig(level=logging.INFO, format=DEFAULT_LOGGING_FORMAT)


class FanoutNamespace(BaseNamespace):
    def on_connect(self):
        logger.info('on connect')
        # NOTE: 这个客户端的问题似乎比较多，我使用 `send` 是没有办法发送的
        self.emit('message', 'message from client')
        self.emit('my_event', 'my event from client')

    def on_disconnect(self):
        logger.info('on disconnect')

    def on_message(self, data):
        logger.info('on message. msg = {}'.format(data))

    def on_my_event(self, data):
        logger.info('on my event. msg = {}'.format(data))


socketIO = SocketIO('127.0.0.1', port=8080)
notificiation_namespace: BaseNamespace = socketIO.define(FanoutNamespace, '/fanout')
notificiation_namespace.emit('my_event', '!!! my event from client')
notificiation_namespace.send('!!! message from client')
notificiation_namespace.emit('message', '!!! message from client')
socketIO.wait()
