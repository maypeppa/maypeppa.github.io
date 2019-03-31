#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import sys

fh = sys.stdin

case_num = int(fh.readline())
for c in range(case_num):
    (sm, ss) = fh.readline().split()
    sm = int(sm)
    res = 0
    cum = 0
    for i in range(sm + 1):
        x = int(ss[i])
        if not x:
            continue
        if cum < i:
            res += i - cum
            cum += (i - cum)
        cum += x
    print('Case #%d: %d' % (c + 1, res))
