#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(n, intervals, ps):
    ans = []
    for p in ps:
        count = 0
        for i in range(n):
            if intervals[2 * i] <= p <= intervals[2 * i + 1]:
                count += 1
        ans.append(count)
    return ans


t = int(input())
for i in range(t):
    n = int(input())
    intervals = [int(x) for x in input().split()]
    p = int(input())
    ps = []
    for _ in range(p):
        ps.append(int(input()))
    input()
    ans = solve(n, intervals, ps)
    print('Case #{}: {}'.format(i + 1, ' '.join([str(x) for x in ans])))
