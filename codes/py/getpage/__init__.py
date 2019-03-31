# -*- coding: utf-8 -*-
#               __                                       
#              /\ \__                                    
#    __      __\ \ ,_\  _____      __       __      __   
#  /'_ `\  /'__`\ \ \/ /\ '__`\  /'__`\   /'_ `\  /'__`\ 
# /\ \L\ \/\  __/\ \ \_\ \ \L\ \/\ \L\.\_/\ \L\ \/\  __/ 
# \ \____ \ \____\\ \__\\ \ ,__/\ \__/.\_\ \____ \ \____\
#  \/___L\ \/____/ \/__/ \ \ \/  \/__/\/_/\/___L\ \/____/
#    /\____/              \ \_\             /\____/      
#    \_/__/                \/_/             \_/__/       

__title__ = 'getpage'
__version__ = '0.1'
__build__ = 0x01
__author__ = 'Liu Shuai'
__copyright__ = 'Copyright 2015 Sogou, Inc.'

from .utils import random_agent, req_args, wait_b4_try, guess_response_encoding
from .page import page_from_resp, Page
from .proxy import get_proxy, report_proxy_status
from .getpage import get

#from .loghandler import CassandraHandler


# Set default logging handler to avoid "No handler found" warnings.
# import logging
# try:  # Python 2.7+
#     from logging import NullHandler
# except ImportError:
#     class NullHandler(logging.Handler):
#         def emit(self, record):
#             pass
# 
# logging.getLogger(__name__).addHandler(NullHandler())
