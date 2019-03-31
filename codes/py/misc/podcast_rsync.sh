#!/usr/bin/env bash
# Copyright (C) dirlt

rsync -avrzL podcast_mp3 hbproxy:~/www/
rsync -avrz podcast_rss hbproxy:~/www/
rsync -avrz podcast_image hbproxy:~/www/
