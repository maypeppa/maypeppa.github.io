#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from collections import defaultdict


class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the number of continuous subarrays whose sum equals to k
    """

    def subarraySumEqualsK(self, nums, k):
        # write your code here

        acc = 0
        map = defaultdict(int)
        res = 0
        for i in range(0, len(nums)):
            acc += nums[i]
            if acc == k:
                res += 1
            comp = acc - k
            res += map[comp]
            map[acc] += 1
        return res
