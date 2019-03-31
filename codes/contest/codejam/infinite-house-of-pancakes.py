#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import sys

fh = sys.stdin
case_num = int(fh.readline())


def f(D, ps):
    bits = [0] * 1001
    for p in ps:
        bits[p] += 1
    mp = max(ps)
    split = 0
    res = mp
    while mp:
        res = min(res, mp + split)
        if mp <= 3:
            break
        p = bits[mp]
        split += p
        x = mp / 2
        y = mp - x
        bits[x] += p
        bits[y] += p
        mp -= 1
        while not bits[mp]:
            mp -= 1
    return res


for c in range(case_num):
    D = int(fh.readline())
    ps = [int(x) for x in fh.readline().split()]
    res = f(D, ps)
    print('Case #%d: %d' % (c + 1, res))
