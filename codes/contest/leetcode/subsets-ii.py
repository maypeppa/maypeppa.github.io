#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        from collections import defaultdict
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        keys = list(d.keys())

        res = [[]]
        for k in keys:
            res2 = []
            for v in range(0, d[k] + 1):
                for r in res:
                    res2.append([k] * v + r)
            res = res2

        return res
