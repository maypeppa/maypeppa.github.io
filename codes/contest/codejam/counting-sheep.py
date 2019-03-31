#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import sys

fh = sys.stdin
case_num = int(fh.readline())


def f(n):
    sv = set()
    seen = set()
    v = n
    while True:
        if v in sv:
            return 'INSOMNIA'
        sv.add(v)
        v2 = v
        while v2:
            seen.add(v2 % 10)
            if len(seen) == 10:
                return v
            v2 /= 10
        v += n


for c in range(case_num):
    n = int(fh.readline())
    res = f(n)
    print(('Case #%d: %s' % (c + 1, res)))
