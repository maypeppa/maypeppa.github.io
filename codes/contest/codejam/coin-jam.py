#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


import sys

fh = sys.stdin


def is_prime(v):
    n = int(v ** 0.5)
    # reduce computation time.
    for x in range(2, 1000):
        if v % x == 0:
            return x
    return 0


def is_jam_coin(ss):
    res = []
    for base in range(2, 11):
        v = int(ss, base)
        x = is_prime(v)
        if not x:
            return None
        res.append(x)
    return res


def gen_coins(bits):
    bits -= 2
    n = 2 ** bits
    for x in range(0, n):
        ss = ''
        for i in range(bits):
            ss += '1' if x % 2 else '0'
            x /= 2
        yield '1' + ss + '1'


def pre_compute():
    d = {}
    for bits in range(2, 32 + 1):
        # print 'bits = %d' % (bits)
        coins = gen_coins(bits)
        res = []
        for c in coins:
            res0 = is_jam_coin(c)
            if not res0:
                continue
            res.append((c, res0))
            if len(res) >= 500:
                break
        d[bits] = res
        # print 'OK'
    return d


d = pre_compute()
case_num = int(fh.readline())
for c in range(case_num):
    (N, J) = [int(x) for x in fh.readline().split()]
    res = d[N][:J]
    print(('Case #%d:' % (c + 1)))
    for (coin, vs) in res:
        print(('%s %s' % (coin, ' '.join([str(x) for x in vs]))))
