#!/usr/bin/env python2
# -*- coding: utf-8 -*- 
import requests
import logging
from .utils import wait_b4_try
from traceback import format_exc

PROXY_HOST_ADDR = 'http://spider.haoma.sogou.com.z.sogou-op.org'
PROXY_GET_PATH = '/get'
PROXY_REPORT_PATH = '/report'

proxy_settings = {
    'HOST': PROXY_HOST_ADDR,
    'GET': PROXY_GET_PATH,
    'REPORT':PROXY_REPORT_PATH,
}

LOG = logging.getLogger(__name__)
#logging.basicConfig(level=logging.DEBUG)
#LOG.addHandler(logging.StreamHandler())

def get_proxy(retry = 3):
    '''
    Try and get the proxies from our proxy service.
    '''
    url = PROXY_HOST_ADDR + PROXY_GET_PATH
    LOG.info('Getting proxy server via ' + url)
    proxy = None
    for i in range(retry):
        # network environment for this should be good
        # so let's wait a little longer
        # instead of overwhealming the server
        wait_b4_try(i)
        try:
            resp = requests.get(url, timeout = 3)
            if resp.status_code != 200:
                LOG.error('Failed to get proxy. Response status code %d.' % resp.status_code)
                continue
            proxy = resp.text
            if len(proxy.split(':')) == 2 and len(proxy.split('.')) == 4:
                # seems like a proxy in ip.ip.ip.ip:port format :)
                break
            else:
                LOG.error('Got proxy in invalid format: ' + resp.text)
        except Exception as e:
            LOG.debug(format_exc())
            LOG.error('Failed to get proxy with exception: ' + str(e))
    if proxy:
        LOG.info('Successfully got proxy: ' + proxy)
        return proxy
    else:
        LOG.error('All %d attempt(s) to get proxy failed. Returning nothing.' % retry)
        return None

def report_proxy_status(proxy, is_valid):
    '''
    Report if the proxy is valid and working to the service.
    
    Will not retry, and the request times out quickly (1s).
    '''
    #assert type(proxy) is str or type(proxy) is unicode
    #assert len(proxy.split('.')) == 4
    #assert len(proxy.split(':')) == 2
    url = PROXY_HOST_ADDR + PROXY_REPORT_PATH
    pl = {'proxy': proxy}
    if is_valid:
        pl['status'] = 'valid'
    else:
        pl['status'] = 'invalid'
    try:
        requests.post(url, data = pl, timeout = 1)
    except:
        LOG.debug(format_exc())
        LOG.error('Failed to report proxy ' + proxy + ' as ' + pl['status'])
    else:
        LOG.info('Reported proxy ' + proxy + ' as ' + pl['status'] + '.')

if __name__ == '__main__':
    print get_proxy()
    print get_proxy()
    print get_proxy()
