#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from collections import defaultdict


def solve(xs):
    cities = []
    cityind = defaultdict(int)
    count = 0
    for (u, w) in xs:
        if u not in cityind:
            cityind[u] = count
            count += 1
            cities.append(u)
        if w not in cityind:
            cityind[w] = count
            count += 1
            cities.append(w)

    adj = [[] for _ in range(count)]
    ind = [0] * count
    for u, w in xs:
        a = cityind[u]
        b = cityind[w]
        adj[a].append(b)
        ind[b] += 1

    ans = []
    start = None
    for x in range(count):
        if ind[x] == 0:
            start = x
            break

    while len(ans) < count:
        ans.append(start)
        tmp = None
        for v in adj[start]:
            ind[v] -= 1
            if ind[v] == 0:
                tmp = v
        start = tmp

    res = []
    for i in range(1, len(ans)):
        x = ans[i - 1]
        y = ans[i]
        res.append('{}-{}'.format(cities[x], cities[y]))
    ans = ' '.join(res)
    return ans


t = int(input())
for i in range(t):
    n = int(input())
    xs = []
    for _ in range(n):
        xs.append((input().strip(), input().strip()))
    ans = solve(xs)
    print('Case #{}: {}'.format(i + 1, ans))
