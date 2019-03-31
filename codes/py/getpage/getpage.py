#!/usr/bin/env python2
# -*- coding: utf-8 -*- 

import requests
import random
import logging

from requests.exceptions import *
from time import time
from traceback import format_exc
from .utils import *
from .page import page_from_resp, Page
from .proxy import get_proxy, report_proxy_status

LOG = logging.getLogger(__name__)

def _get_page_requests(url, proxy = '', fpfirst = False, headers = None):
    '''
    Get the page using native package requests.

    Note: only http schema is currently supported.
    '''
    LOG.info('Trying to get page %s via requests, proxy %s.' % (url, proxy or 'N/A'))
    start_ts = time()
    session = requests.Session()
    rargs = req_args()
    if headers:
        rargs['headers'].update(headers)
    # TODO: assuming http schema. should check.
    if proxy:
        rargs['proxies'] = {'http': 'http://' + proxy}

    resp = None
    try:
        # some sites needs cookies from the frontpage
        if fpfirst:
            urlsplit = url.split('/')
            if len(urlsplit) > 3 and urlsplit[3] != '':
                fpurl = urlsplit[0] + '//' +urlsplit[2]
                resp = session.get(fpurl, **rargs)
                # sleep some random time before requesting again
                sleep(random.uniform(2, 4))
        resp = session.get(url, **rargs)
    except RequestException as e:
        LOG.info(str(e))
    except Exception as e:
        LOG.critical('Unexpected exceptions encountered.')
        LOG.critical(str(e))
        LOG.debug(format_exc())

    if not resp and proxy:
        LOG.warning('Proxy failed while getting page %s. Proxies: %s' % (url, proxy))
        report_proxy_status(proxy, False)
    elif resp and proxy:
        report_proxy_status(proxy, True)

    if not resp:
        return None

    status = resp.status_code / 100
    if status == 4:
        LOG.info('Page not found or request error (%d) while getting page %s.' % (resp.status_code, url))
        LOG.info('Time elapsed: %gs. Returning nothing.' % (time() - start_ts))
        return None
    elif status == 5:
        LOG.info('Server error (%d) while getting page %s.' % (resp.status_code, url))
        LOG.info('Time elapsed: %gs. Returning nothing.' % (time() - start_ts))
        return None
    elif status != 2:
        LOG.info('Got response with status code %d while getting page %s.' % (resp.status_code, url))
        return None

    # page got successfully, andeverything looks good so far
    # requests automatically decompresses gzip-encoded responses
    # so we're good
    elapsed = time() - start_ts
    LOG.info('Successfully got page %s in %gs.' % (url, elapsed))
    p = page_from_resp(resp)
    p.elapsed = elapsed
    p.proxy = proxy
    p.req_url = url
    return p

def _get_page_phantomjs(url, proxy = ''):
    '''
    Get the page using phantomjs.

    Note: only http schema is currently supported.
    '''
    LOG.info('Trying to get page %s via PhantomJS, proxy %s.' % (url, proxy or 'N/A'))
    start_ts = time()
    import os
    jspath = os.path.join(os.path.dirname(__file__), 'get.js')
    content = check_output(['phantomjs', '--proxy='+proxy, jspath, url])
    elapsed = time() - start_ts

    if content:
        LOG.info('Successfully got page %s in %gs.' % (url, elapsed))
        if proxy:
            report_proxy_status(proxy, True)
    else:
        LOG.warning('Failed to get page %s in %gs, yet we can\'t know what happened.' % (url, elapsed))
        if proxy:
            report_proxy_status(proxy, False)
        return None

    enc = guess_content_encoding(content)
    p = Page(url, content, enc)
    p.elapsed = elapsed
    p.proxy = proxy
    p.req_url = url
    return p

def get(url, retry = 3, fpfirst = False, use_proxy = True, render_js = False, headers = None):
    """
    Download a web page via proxy and return as unicode string.

    A proxy server is automatically retrieved from server
    and used, unless use_proxy is set to False, where the page
    will be fetched directly. The proxy status is reported back
    to server after each successful or failed use.

    Note: JavaScript renderer is not currently supported.
    """
    schema = url.split('://')[0]
    if schema == url:
        LOG.warning('URL schema missing. Assuming HTTP.')
        url = 'http://' + url
    elif schema not in ('http', 'https',): # 'https', 'ftp'):
        LOG.error('URL schema "%s" not supported. Returning nothing.' % schema)
        return None

    if render_js and (fpfirst or headers != None):
        LOG.error('fpfirst and headers are not supported when render_js is specified. Ignoring.')

    for i in range(retry):
        if use_proxy:
            proxy = get_proxy()
            if not proxy:
                LOG.warning('No valid proxy to get page. Continuing.')
                continue
        else:
            wait_b4_try(i)
            proxy = ''
        if render_js:
            p = _get_page_phantomjs(url, proxy)
        else:
            p = _get_page_requests(url, proxy, fpfirst, headers)
        if p:
            return p
    return None

if __name__ == '__main__':
    LOG.addHandler(logging.StreamHandler())
    logging.basicConfig(level = logging.INFO)
    p = get('http://cnbeta.com')
    if p:
        print 'url', p.url
        print 'encoding', p.encoding
        print 'text', p.text[:1000]
        print 'elapsed', p.elapsed
    else:
        print 'None'
