#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import sys

fh = sys.stdin
case_num = int(fh.readline())

for c in range(case_num):
    s = fh.readline().strip()
    s2 = ' '.join(s.split()[::-1])
    print('Case #%d: %s' % (c + 1, s2))
