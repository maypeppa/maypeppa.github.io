#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import itertools


def f(fwd):
    n = len(fwd)
    res = 0
    for arr in itertools.permutations(list(range(n))):
        for i in range(1, n):
            x = arr[i - 1]
            y = arr[i]
            z = arr[0]
            u = arr[1]
            if (fwd[y] == x or fwd[y] == z) and \
                    (fwd[z] == u or fwd[z] == y):
                res = max(res, i + 1)
            if (i + 1) != n and not (fwd[y] == x or fwd[y] == arr[i + 1]):
                break
        if res == n:
            break
    return res


import sys

fh = sys.stdin
case_n = int(fh.readline())

for c in range(case_n):
    n = int(fh.readline())
    arr = [int(x) for x in fh.readline().strip().split(' ')]
    fwd = [0] * n
    for (idx, v) in enumerate(arr):
        fwd[idx] = v - 1
    res = f(fwd)
    print(('Case #%d: %d' % (c + 1, res)))
