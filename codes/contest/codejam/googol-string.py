#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(k):
    n = 1
    k -= 1
    while n <= k:
        n = n * 2 + 1

    flip = 0
    ans = 0
    while True:
        if k == (n // 2):
            break
        elif k < (n // 2):
            n = n // 2
        else:
            flip = 1 - flip
            k = n - 1 - k
    if flip:
        ans = 1 - ans
    return ans


t = int(input())
for i in range(t):
    k = int(input())
    ans = solve(k)
    print('Case #{}: {}'.format(i + 1, ans))
