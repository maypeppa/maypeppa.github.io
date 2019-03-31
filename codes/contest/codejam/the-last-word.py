#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import sys

fh = sys.stdin
case_n = int(fh.readline())


def f(s):
    res = ''
    for x in s:
        ss = max(res + x, x + res)
        res = ss
    return res


for c in range(case_n):
    s = fh.readline().strip()
    res = f(s)
    print(('Case #%d: %s' % (c + 1, res)))
