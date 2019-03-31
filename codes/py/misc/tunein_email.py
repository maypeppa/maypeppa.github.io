#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import pymongo
import snappy
import requests
from bs4 import BeautifulSoup
import hashlib
import bson
import json
import time

client = pymongo.MongoClient()
cache_table = client.test.cache_table

urls = """Canada http://tunein.com/radio/Canada-r101227/
Australia http://tunein.com/radio/Australia-r101356/
Mexico http://tunein.com/radio/Mexico-r101271/
Argentina http://tunein.com/radio/Argentina-r100294/
New-Zealand http://tunein.com/radio/New-Zealand-r101279/
United-Arab-Emirates http://tunein.com/radio/United-Arab-Emirates-r100435/
South-Korea http://tunein.com/radio/South-Korea-r100367/
Malaysia http://tunein.com/radio/Malaysia-r101265/
Taiwan http://tunein.com/radio/Taiwan-r101302/
Singapore http://tunein.com/radio/Singapore-r101293/
Israel http://tunein.com/radio/Israel-r100358/
India http://tunein.com/radio/India-r100355/
Indonesia http://tunein.com/radio/Indonesia-r100356/
Hong-Kong http://tunein.com/radio/Hong-Kong-r100354/
United-Kingdom http://tunein.com/radio/United-Kingdom-r101309/
Italy http://tunein.com/radio/Italy-r100359/
Greece http://tunein.com/radio/Greece-r101244/
Spain http://tunein.com/radio/Spain-r100416/
Ukraine http://tunein.com/radio/Ukraine-r100434/
Turkey http://tunein.com/radio/Turkey-r101308/
Switzerland http://tunein.com/radio/Switzerland-r100422/
Sweden http://tunein.com/radio/Sweden-r101300/
Norway http://tunein.com/radio/Norway-r100392/
Czech-Republic http://tunein.com/radio/Czech-Republic-r101232/
Netherlands http://tunein.com/radio/Netherlands-r100385/
Finland http://tunein.com/radio/Finland-r101239/
France http://tunein.com/radio/France-r101240/
Russia http://tunein.com/radio/Russia-r100401/
Germany http://tunein.com/radio/Germany-r100346/
Denmark http://tunein.com/radio/Denmark-r101233/
Belgium http://tunein.com/radio/Belgium-r100304/
Austria http://tunein.com/radio/Austria-r101221/
United-States http://tunein.com/radio/United-States-r100436/""".split('\n')

urls = [[y.strip() for y in x.split()] for x in urls]

class SessionThrottle(object):
    def __init__(self, rate_limit):
        self.rate_limit = rate_limit
        self.rate_cnt = 0
        self.rate_ts = time.time()

    def set_rate_limit(self, v):
        self.rate_limit = v

    def run(self):
        if self.rate_limit:
            now_ts = time.time()
            ts = self.rate_cnt / self.rate_limit
            self.rate_cnt += 1
            delay = ts - (now_ts - self.rate_ts)
            if delay > 0.1:
                time.sleep(delay)
                return delay
        return 0

throttle = SessionThrottle(2)

def get_sha1_key(s):
    return hashlib.sha1(s).hexdigest()

def _get(key, callback, args):
    r = cache_table.find_one({'_id': key})
    if not r:
        content = callback(*args)
        data = bson.binary.Binary(snappy.compress(content))
        cache_table.insert_one({'_id': key, 'data': data})
    else:
        data = r['data']
    content = snappy.decompress(data)
    return content

def request_url_callback(url):
    throttle.run()
    r = requests.get(url)
    return r.content

def parse_url_callback(url, selector):
    content = _get(get_sha1_key(url), request_url_callback, (url, ))
    bs = BeautifulSoup(content)
    xs = [x.attrs['href'] for x in bs.select(selector)]
    content = json.dumps(xs)
    return content

def get_states(url):
    key = get_sha1_key('tunein-state-' + url)
    content = _get(key, parse_url_callback, (url, '#mainContent > div > div.group.clearfix.linkmatrix > ul > li > a'))
    xs = json.loads(content)
    links = ['http://tunein.com' + x for x in xs]
    return links

def get_stations(url):
    key = get_sha1_key('tunein-station-' + url)
    content = _get(key, parse_url_callback, (url, '#mainContent > div > div > ul > li > a'))
    xs = json.loads(content)
    links = ['http://tunein.com' + x for x in xs]
    return links

import re
EMAIL_REGEX = re.compile(r'mailto:([^"]+)')
def get_email(url):
    ct = _get(get_sha1_key(url), request_url_callback, (url, ))
    m = EMAIL_REGEX.search(ct)
    if m: return m.groups()[0]
    return None

import json
import os

def main():
    d = {}
    cid = -1
    call = len(urls)
    for (country, url) in urls:
        cid += 1
        emails = set()
        states = get_states(url)
        print('extending states ...')
        # what if we have more than two level states.
        states2 = []
        states2.extend(states)
        for s in states:
            states2.extend(get_states(s))
        states = list(set(states2))
        print('country = %s[%d/%d], states = %d' % (country, cid, call, len(states)))
        rall = len(states)
        for (rid, state) in enumerate(states):
            stations = get_stations(state)
            print('country = %s[%d/%d], state = %s[%d/%d], stations = %d' % (
                country, cid, call, state, rid, rall, len(stations)))
            for st in stations:
                email = get_email(st)
                if not email: continue
                emails.add(email)
        d[country] = list(emails)
        print('country = %s, emails = %d' % (country, len(emails)))

    with open('tunein-email.txt', 'w') as fh:
        for key in d:
            emails = d[key]
            lines = list(emails)
            lines.insert(0, '>>>>> country (%s) <<<<<' % key)
            fh.writelines([x + '\n' for x in lines])

if __name__ == '__main__':
    main()
