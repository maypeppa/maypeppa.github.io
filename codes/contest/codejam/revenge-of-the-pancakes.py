#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import sys

fh = sys.stdin
case_num = int(fh.readline())


def flip_one(ss, target):
    idx = len(ss) - 1
    while idx >= 0 and ss[idx] == target:
        idx -= 1
    return idx


def flip(ss):
    target = '+'
    res = 0
    while True:
        idx = flip_one(ss, target)
        if idx == -1:
            break
        res += 1
        ss = ss[:idx]
        target = '-' if target == '+' else '+'
    return res


for c in range(case_num):
    ss = fh.readline().strip()
    res = flip(ss)
    print(('Case #%d: %d' % (c + 1, res)))
