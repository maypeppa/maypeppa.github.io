#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def ip2tocdr(start, end):
    def zeros(x):
        cnt = 0
        while x & 0x1 == 0:
            cnt += 1
            x >>= 1
        return cnt

    x = start
    res = []
    while x <= end:
        zs = zeros(x)
        while (x + (1 << zs) - 1) > end:
            zs -= 1
        res.append((x, 32 - zs))
        x += (1 << zs)
    return res


if __name__ == '__main__':
    res = ip2tocdr(1, 14)
    print(res)
