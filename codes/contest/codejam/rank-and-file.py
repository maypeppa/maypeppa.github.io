#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import sys

fh = sys.stdin
case_n = int(fh.readline())

for c in range(case_n):
    n = int(fh.readline())
    d = {}
    for i in range(2 * n - 1):
        vs = [int(x) for x in fh.readline().split()]
        for v in vs:
            d[v] = d.get(v, 0) + 1
    res = []
    for k in d:
        if d[k] % 2:
            res.append(k)
    res.sort()
    assert (len(res) == n)
    print(('Case #%d: %s' % (c + 1, ' '.join([str(x) for x in res]))))
