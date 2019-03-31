#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import bisect


class Solution:
    """
    @param citations: a list of integers
    @return: return a integer
    """

    def hIndex(self, citations):
        # write your code here

        citations.sort()
        n = len(citations)
        for h in range(n, 0, -1):
            idx = bisect.bisect_left(citations, h)
            if (n - idx) >= h:
                return h
        return 0
