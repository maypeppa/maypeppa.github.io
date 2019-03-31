#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(x):
    a = x
    count = 0
    while a:
        a = a // 10
        count += 1

    def dist(x, digit, count):
        z = digit
        for _ in range(count):
            z = z * 10 + 8
        return x - z

    base = 10 ** count
    while base:
        a = x // base
        if a % 2 == 1:
            if a == 9:
                return dist(x, 8, count)
            else:
                return min(dist(x, a - 1, count),
                           (a + 1) * (10 ** count) - x)
        x = x % base
        base = base // 10
        count -= 1
    return 0


t = int(input())
for i in range(t):
    x = int(input())
    ans = solve(x)
    print('Case #{}: {}'.format(i + 1, ans))
