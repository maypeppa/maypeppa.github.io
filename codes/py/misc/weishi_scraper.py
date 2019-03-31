#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import brotli
import glob
import json
import os
import requests

USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 MicroMessenger/6.7.4(0x1607042c) NetType/WIFI Language/zh_CN'


class WeishiScraper(object):
    def __init__(self, working_dir, cookie=None):
        self.workdir = working_dir
        self.cookie = cookie
        self.courses = []

    def load_courses(self):
        dir = os.path.join(self.workdir, 'courses')
        files = glob.glob(dir + '/*')
        courses = []
        for file in files:
            with open(file, 'rb') as fh:
                raw_data = fh.read()
                data = brotli.decompress(raw_data)
                js = json.loads(data)
                courses.extend(js['data']['courses'])
        self.courses = courses

    def get_audio_url(course_id):
        url = 'https://m.weishi100.com/m/audioCourse/info?courseId={}'.format(course_id)
        referer = 'https://m.weishi100.com/mweb/single/?id={}'.format(course_id)
        headers = {
            'User-Agent': USER_AGENT,
            'Cookie': self.cookie,
            'Referer': referer
        }
        resp = requests.get(url, headers=headers)
        raw_data = resp.content
        print(raw_data)
        # data = brotli.decompress(raw_data)
        js = json.loads(raw_data)
        try:
            audio_url = js['data']['audioUrl']
        except:
            audio_url = None
            print(js)
        print('course_id = {}, url = {}'.format(course_id, audio_url))
        return audio_url

    def walk_courses(self):
        for c in self.courses:
            course_id = c['id']
            audio_url = self.get_audio_url(course_id)
            c['audioUrl'] = audio_url

    def save_ckpt(self):
        path = os.path.join(self.workdir, 'ckpt.json')
        with open(path, 'w') as fh:
            json.dump(self.courses, fh)

    def load_ckpt(self):
        path = os.path.join(self.workdir, 'ckpt.json')
        with open(path, 'r') as fh:
            self.courses = json.load(fh)

    def gen_download_script(self):
        path = os.path.join(self.workdir, 'download.sh')
        audio_path = os.path.join(self.workdir, 'audio')
        os.makedirs(audio_path, exist_ok=True)
        with open(path, 'w') as fh:
            for c in self.courses:
                fh.write('wget --continue "{}" -O "{}/{}.mp3"\n'.format(c['audioUrl'], audio_path, c['name']))
