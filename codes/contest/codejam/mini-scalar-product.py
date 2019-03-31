#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import sys

fh = sys.stdin
case_num = int(fh.readline())

for c in range(case_num):
    n = int(fh.readline())
    xs = [int(x) for x in fh.readline().split()]
    ys = [int(x) for x in fh.readline().split()]
    xs.sort()
    ys.sort()
    res = 0
    for idx in range(n):
        res += xs[idx] * ys[n - 1 - idx]
    print('Case #%d: %d' % (c + 1, res))
