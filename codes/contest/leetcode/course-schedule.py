#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        n = numCourses
        edges = []
        ins = [0] * n
        for i in range(n):
            edges.append([])

        for p in prerequisites:
            u = p[0]
            v = p[1]
            edges[v].append(u)
            ins[u] += 1

        orders = []
        lookup = set(range(n))
        while lookup:
            u2 = None
            for u in lookup:
                if ins[u] == 0:
                    u2 = u
                    break
            if u2 is None:
                return False
            u = u2
            orders.append(u)
            for v in edges[u]:
                ins[v] -= 1
            lookup.remove(u)
        return True
