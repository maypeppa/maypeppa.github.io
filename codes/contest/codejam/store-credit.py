#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import functools
import sys

fh = sys.stdin
case_num = int(fh.readline())


def bs(items, x, ct):
    s = 0
    e = len(items) - 1
    while (s <= e):
        m = (s + e) / 2
        if items[m][1] == x:
            if items[m][0] == ct:
                s = s + 1
            else:
                return m
        elif items[m][1] > x:
            e = e - 1
        else:
            s = s + 1
    return -1


def cmp(x, y):
    if x < y: return -1
    if x > y: return 1
    return 0


for c in range(case_num):
    C = int(fh.readline())
    I = int(fh.readline())
    items = [(x[0] + 1, int(x[1])) for x in enumerate(fh.readline().split())]
    items.sort(key=functools.cmp_to_key(lambda x, y: cmp(x[1], y[1])))
    for x in items:
        if x[1] >= C:
            continue
        m = bs(items, C - x[1], x[0])
        if m != -1:
            y = items[m]
            (a, b) = (x[0], y[0])
            if a > b:
                (a, b) = (b, a)
            print('Case #%d: %d %d' % (c + 1, a, b))
            break
