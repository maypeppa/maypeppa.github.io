#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import logging
import os

from flask import Flask, request, session
from flask_socketio import Namespace, SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, message_queue='redis://localhost/0', channel='flask-socketio')
logger = logging.getLogger('server')
DEFAULT_LOGGING_FORMAT = '[%(asctime)s][%(levelname)s]%(filename)s@%(lineno)d: %(msg)s'
logging.basicConfig(level=logging.INFO, format=DEFAULT_LOGGING_FORMAT)


@app.route('/fanout', methods=['GET'])
def index():
    room = request.args.get('room', 0)
    logging.info(request.environ['REMOTE_ADDR'], request.environ['REMOTE_PORT'], room)
    # return render_template('index.html')
    return 'OK'


class FanoutNamespace(Namespace):
    path = '/fanout.%s' % (os.getpid())

    def on_connect(self):
        logger.info('path = {}, on connect sid = {}, ({}:{})'.format(
            self.path, request.sid, request.environ['REMOTE_ADDR'],
            request.environ['REMOTE_PORT']))

        socketio.send('message: connect OK to all', namespace='/fanout')
        socketio.emit('my event', 'my event: connect OK', namespace='/fanout')
        session['data'] = request.sid

    def on_disconnect(self):
        logger.info('path = {}, on disconnect. session data = {}'.format(self.path, session['data']))

    def on_message(self, message):
        logger.info('path = {}, on message. msg = {}'.format(self.path, message))

    def on_my_event(self, message):
        logger.info('path = {}, on my event. msg = {}'.format(self.path, message))


socketio.on_namespace(FanoutNamespace('/fanout'))

if __name__ == '__main__':
    import sys

    port = 8080
    if len(sys.argv) >= 2:
        port = int(sys.argv[1])
    socketio.run(app, debug=True, port=port)
