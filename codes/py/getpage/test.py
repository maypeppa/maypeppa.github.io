#!/usr/bin/env python2

import logging
import unittest

from . import getpage
from .page import Page

LOG = logging.getLogger(__name__)
logging.basicConfig(level = logging.DEBUG)

class TestGetPageQuick(unittest.TestCase):
    def printPage(self, p):
        print '===================================='
        if p:
            print 'url\':\t', p.url
            print 'enc:\t', p.encoding
            print 'text:\t', p.text.strip()[:200]
            print 'len:\t', len(p.text)
            print 'time:\t', p.elapsed
            print 'proxy:\t', p.proxy
            self.assertEqual(p.content.decode(p.encoding), p.text)
        else:
            print '(None)'

    def setUp(self):
        self.urls = [
            # encoding not specifid in http header
            'http://cnbeta.com',
            # wetern europe
            'http://www.bundesregierung.de/Webs/Breg/EN/Homepage/_node.html',
            'http://de.wikipedia.org/wiki/Wikipedia:Hauptseite',
            # locoso page
            'http://www.locoso.com/company/tm70v0t',
            'http://www.locoso.com/cate/bjbqh',
            'http://www.locoso.com/cate/bjbqh/cho1h1',
            'http://www.locoso.com/cate/bjbqh/7/cho1h1',
            # non-existent page (404)
            'http://www.locoso.com/company/m6s0v27', 
            'http://www.locoso.com/cony/m20ls70v27', 
            # unsupported schema
            'https://www.suse.com/de-de/',
            # no schema
            'cnbeta.com',
            'www.suse.com/de-de/',
            # locoso page
            # non-existent site
            'http://asdfjklasdfjklasdfjkl.com',
            # other pages
            'http://aws.caperea.com/Cassandra',
        ]
        self.proxies = [
            '186.200.166.178:8080',
        ]

    def test_quick(self):
        url = 'http://www.cnbeta.com/articles/372623.htm'
        print 'Quick test'
        print '===================================='
        print 'PX: N, FP: N, JS: N'
        p = getpage.get(url, use_proxy=False, fpfirst=False, render_js=False)
        self.printPage(p)
        print '===================================='
        print 'PX: N, FP: Y, JS: N'
        p = getpage.get(url, use_proxy=False, fpfirst=True, render_js=False)
        self.printPage(p)
        print '===================================='
        print 'PX: N, FP: Y, JS: Y'
        p = getpage.get(url, use_proxy=False, fpfirst=True, render_js=True)
        self.printPage(p)

        print '===================================='
        print 'PX: Y, FP: N, JS: N'
        p = getpage.get(url, use_proxy=True, fpfirst=True, render_js=False)
        self.printPage(p)
        print '===================================='
        print 'PX: Y, FP: Y, JS: Y'
        p = getpage.get(url, use_proxy=True, fpfirst=True, render_js=True)
        self.printPage(p)

    def runTest(self):
        self.test_quick()


class TestGetPage(TestGetPageQuick):
    def test_get_page_no_proxy(self):
        print 'Testing _get_page() w/o proxy...'
        for url in self.urls:
            print '===================================='
            print 'url:\t', url
            p = getpage._get_page(url)
            self.printPage(p)
            self.assertTrue(type(p) is Page or p is None)

    def test_get_batch(self):
        print 'Batch testing get() w/ proxy...'
        for url in self.urls:
            print '===================================='
            print 'url:\t', url
            p = getpage.get(url)
            self.printPage(p)
            self.assertTrue(type(p) is Page or p is None)

    def test_get(self):
        print '===================================='
        print '===================================='
        print '===================================='
        print 'Testing get()...'
        print '===================================='
        url = 'http://www.cnbeta.com/articles/372623.htm'
        print '===================================='
        p = getpage.get(url, retry=1, use_proxy=False, fpfirst=False, render_js=False)
        self.printPage(p)
        print '===================================='
        p = getpage.get(url, retry=1, use_proxy=False, fpfirst=True, render_js=False)
        self.printPage(p)
        print '===================================='
        p = getpage.get(url, retry=1, use_proxy=False, fpfirst=True, render_js=True)
        self.printPage(p)
        print '===================================='
        p = getpage.get(url, retry=2, use_proxy=True, fpfirst=False, render_js=False)
        self.printPage(p)
        print '===================================='
        p = getpage.get(url, retry=2, use_proxy=True, fpfirst=True, render_js=False)
        self.printPage(p)
        print '===================================='
        p = getpage.get(url, retry=2, use_proxy=True, fpfirst=True, render_js=True)
        self.printPage(p)
        print '===================================='


        
if __name__ == '__main__':
    #unittest.main()
    t = TestGetPageQuick()
    t.test_quick()
