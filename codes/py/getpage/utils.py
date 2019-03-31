#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import logging
import random
from time import sleep, clock
from chardet import detect
from re import search
from requests.utils import get_encodings_from_content, get_encoding_from_headers
from subprocess import Popen, PIPE

LOG = logging.getLogger(__name__)
REQUEST_TIMEOUT = 30 # second(s)

def random_agent():
    REAL_WORLD_AGENTS = (
        # Linux
        '5.0 (X11; Linux x86_64; rv:29.0) Gecko/20100101 Firefox/29.0',
        '5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36',
        # Mac
        '5.0 (Macintosh; Intel Mac OS X 10.9; rv:29.0) Gecko/20100101 Firefox/29.0',
        '5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36',
        'Mac / Safari 7: 5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14',
        # Windows
        '5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0',
        '5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36',
        '4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',
        '4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        '4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0)',
        '5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
        '5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
        '5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        # Android
        #'5.0 (Android; Mobile; rv:29.0) Gecko/29.0 Firefox/29.0',
        #'5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36',
        # iOS
        #'5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) CriOS/34.0.1847.18 Mobile/11B554a Safari/9537.53',
        #'5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53', )
        )
    return 'Mozilla/' + random.choice(REAL_WORLD_AGENTS)

def req_args():
    '''
    Build request arguments as kwargs for requests.get
    '''
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': random_agent(),
        #connection
        #cache control
        #pragma
    }
    return {'timeout': REQUEST_TIMEOUT, 'headers': headers}

def guess_response_encoding(resp):
    '''
    Guess the content encoding of a requests response.

    Note: there's a performance issue due to chardet.
    '''
    # first try the encoding supplied by responce header and content
    encs = get_encodings_from_content(resp.content) or []
    for enc in encs:
        try:
            resp.content.decode(enc)
            LOG.info('Detected encoding %s from response content.', enc)
            return enc
        except UnicodeDecodeError:
            LOG.debug('Encoding from response content doesn\'t work.')

    enc = get_encoding_from_headers(resp.headers)
    if enc:
        try:
            resp.content.decode(enc)
            LOG.info('Detected encoding %s from response header.', enc)
            return enc
        except UnicodeDecodeError:
            LOG.debug('Encoding from response header doesn\'t work.')

    # neither encoding works, we have to go the hard way.
    start = clock()
    g = detect(resp.content)
    LOG.info('Detected encoding %s with cofidence of %g in %gs.' % (g['encoding'], g['confidence'], clock() - start))
    return g['encoding']

def guess_content_encoding(content):
    '''
    Guess the encoding for plain content.

    Note: there's a performance issue due to chardet.
    '''
    # first try the encoding supplied by content
    encs = get_encodings_from_content(content) or []
    for enc in encs:
        try:
            content.decode(enc)
            LOG.info('Detected encoding %s from content.', enc)
            return enc
        except UnicodeDecodeError:
            LOG.debug('Encoding from content doesn\'t work.')

    # neither encoding works, we have to go the hard way.
    start = clock()
    g = detect(content)
    LOG.info('Detected encoding %s with cofidence of %g in %gs.' % (g['encoding'], g['confidence'], clock() - start))
    return g['encoding']

def wait_b4_try(num_tried, base = 1):
    '''
    Wait befor trying, ONLY if needed. Base intverval in seconds.

    Waiting time is determied by number of previous attempts -
    it DOUBLES with every attempt you've made.
    Of course we won't wait on the first try.
    '''
    if num_tried:
        t = 2 ** (num_tried - 1) * base
        LOG.info('Sleeping for %f seconds' % t)
        sleep(t)

def check_output(*popenargs, **kwargs):
    r"""Run command with arguments and return its output as a byte string.

    If the exit code was non-zero it raises a CalledProcessError.  The
    CalledProcessError object will have the return code in the returncode
    attribute and output in the output attribute.

    The arguments are the same as for the Popen constructor.  Example:

    >>> check_output(["ls", "-l", "/dev/null"])
    'crw-rw-rw- 1 root root 1, 3 Oct 18  2007 /dev/null\n'

    The stdout argument is not allowed as it is used internally.
    To capture standard error in the result, use stderr=STDOUT.

    >>> check_output(["/bin/sh", "-c",
    ...               "ls -l non_existent_file ; exit 0"],
    ...              stderr=STDOUT)
    'ls: non_existent_file: No such file or directory\n'
    """
    process = Popen(stdout=PIPE, *popenargs, **kwargs)
    output, unused_err = process.communicate()
    retcode = process.poll()
    if retcode:
        return None
    return output

if __name__ == '__main__':
    logging.basicConfig(level = logging.DEBUG)
    wait_b4_try(1, 0.1)
    print random_agent()

    wait_b4_try(2, 0.1)
    print req_args()

    import requests
    wait_b4_try(3, 0.1)
    r = requests.get('http://cnbeta.com')
    print guess_response_encoding(r)
