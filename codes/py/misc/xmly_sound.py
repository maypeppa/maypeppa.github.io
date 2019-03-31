#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from __future__ import (absolute_import, division, print_function, unicode_literals)

import requests
from bs4 import BeautifulSoup
import json

def parse_sound_id_list(data):
    bs = BeautifulSoup(data, 'html.parser')
    nodes = bs.select('.album_soundlist > ul > li')
    id_list = [x.attrs['sound_id'] for x in nodes]
    return id_list

def parse_sound_info(data):
    data = data.decode('utf8')
    js = json.loads(data)
    title = js['title']
    play_url = js['play_path']
    return (title, play_url)

def make_sound_info_url(sound_id):
    return 'http://www.ximalaya.com/tracks/%s.json' % sound_id

def get_docs(url):
    ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    r = requests.get(url, headers = {'User-Agent': ua})
    sound_id_list = parse_sound_id_list(r.content)
    docs = []
    for sound_id in sound_id_list:
        sound_info_url = make_sound_info_url(sound_id)
        print(sound_info_url)
        r = requests.get(sound_info_url, headers = {'User-Agent': ua})
        (title, play_url) = parse_sound_info(r.content)
        docs.append((title, play_url))
    return docs

def write_script(docs):
    with open('download.sh', 'w') as fh:
        for (title, play_url) in docs:
            cmd = 'wget -nc -O "%s.mp3" %s' % (title, play_url)
            fh.write(cmd + '\n')

def main(urls):
    all_docs = []
    for url in urls:
        docs = get_docs(url)
        all_docs.extend(docs)
    write_script(all_docs, file_prefix)

urls = ['http://www.ximalaya.com/1000202/album/61/']
main(urls)
