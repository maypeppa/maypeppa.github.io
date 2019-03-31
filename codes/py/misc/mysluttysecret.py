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

urls = ['http://mysluttysecret.com/',
        'http://mysluttysecret.com/page/2/']

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
    return hashlib.sha1(s.encode('utf8')).hexdigest()

def _get(url, callback, *args):
    key = get_sha1_key(url)
    r = cache_table.find_one({'_id': key})
    if not r:
        throttle.run()
        r = requests.get(url)
        content = callback(r, *args)
        data = bson.binary.Binary(snappy.compress(content))
        cache_table.insert_one({'_id': key, 'data': data})
    else:
        data = r['data']
    content = snappy.decompress(data)
    return content

def parse_url_callback(r, selector):
    bs = BeautifulSoup(r.content)
    xs = list([x.attrs['href'] for x in bs.select(selector)])
    content = json.dumps(xs)
    return content

def get_posts(url):
    content = _get(url, parse_url_callback, 'article > header > h2 > a')
    links = json.loads(content)
    return links

def get_post(url):
    content = _get(url, lambda r: r.content)
    bs = BeautifulSoup(content)
    title = bs.select('article > header > .entry-title')[0].text
    image = bs.select('article > div.single-thumb > a > img')[0].attrs['src']
    audio = bs.select('audio > source')[0].attrs['src']
    desc = bs.select('article > div.entry-content > p')[0].text
    return (title, image, audio, desc)

import json
import os

def download(url, local):
    if os.path.exists(local): return
    with open(local, 'wb') as fh:
        r = requests.get(url)
        fh.write(r.content)

def main():
    docs = []
    for url in urls:
        print(url)
        posts = get_posts(url)
        for p in posts:
            print('>>>', p)
            d = get_post(p)
            docs.append(d)
    docs = docs[::-1]

    shell = []
    with open('mysluttysecret.txt', 'w') as fh:
        for (idx, d) in enumerate(docs):
            (title, image, audio, desc) = d
            title = title.encode('utf8')
            desc = desc.encode('utf8')
            fh.write('---- # %d -----\n' % (idx + 1))
            fh.write('%s\n%s\n\n\n' % (title, desc))

            img = 'myss/%d.png' % (idx + 1)
            shell.append('if [ ! -f %s ]; then wget "%s" -O %s; fi' % (img, image, img))
            aud = 'myss/%d.m4a' % (idx + 1)
            shell.append('if [ ! -f %s ]; then wget "%s" -O %s; fi' % (aud, audio, aud))

    with open('mysluttysecret.sh', 'w') as fh:
        fh.writelines([x + '\n' for x in shell])

if __name__ == '__main__':
    main()
