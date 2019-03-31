#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param points: a 2D array
    @return: the number of boomerangs
    """

    def numberOfBoomerangs(self, points):
        # Write your code here

        def dist_square(x, y):
            return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2

        res = 0
        for i in range(len(points)):
            map = dict()
            for j in range(0, len(points)):
                if j == i: continue
                value = dist_square(points[i], points[j])
                if value not in map:
                    map[value] = 1
                else:
                    map[value] += 1
            for cnt in map.values():
                res += cnt * (cnt - 1)
        return res
