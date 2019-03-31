#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """

    def insert(self, intervals, newInterval):
        # write your code here

        xs = intervals
        ys = [newInterval]
        res = []
        x, y = 0, 0
        prev = None
        while x < len(xs) or y < len(ys):
            xi = xs[x] if x < len(xs) else None
            yi = ys[y] if y < len(ys) else None
            if xi and yi:
                if xi.start < yi.start:
                    p = xi
                    x += 1
                else:
                    p = yi
                    y += 1
            else:
                if xi:
                    p = xi
                    x += 1
                else:
                    p = yi
                    y += 1

            if prev is None:
                prev = Interval(p.start, p.end)
            else:
                if p.start <= prev.end:
                    prev.end = max(p.end, prev.end)
                else:
                    res.append(prev)
                    prev = Interval(p.start, p.end)
        if prev:
            res.append(prev)
        return res
