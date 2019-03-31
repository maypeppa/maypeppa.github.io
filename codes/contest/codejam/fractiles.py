#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import sys

fh = sys.stdin
case_num = int(fh.readline())

"""
这个问题我的想法考虑一个通用情况, 假设original tiles长度是k. 假设在0th, (i-1)th, (j-1)th是G的话，
分别考虑C=2,C=3的时候，应该在哪个点clean是最优解. 如果C=3的话，那么三个G会共同出现在一个位置上，就是0 * k^2 + (i-1) *k + (j-1)
以此类推，如果C=K的话，那么所有可能的G都会出现在一点上.
"""


def f(k, c, s):
    if c * s < k:
        return 'IMPOSSIBLE'
    res = []
    for i in range(0, k, c):
        x = 0
        for j in range(i, min(i + c, k)):
            x = x * k + j
        res.append(x + 1)
    return ' '.join([str(x) for x in res])


for c in range(case_num):
    (K, C, S) = [int(x) for x in fh.readline().split()]
    res = f(K, C, S)
    print(('Case #%d: %s' % (c + 1, res)))
