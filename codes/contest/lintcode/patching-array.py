#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param nums: an array
    @param n: an integer
    @return: the minimum number of patches required
    """

    def minPatches(self, nums, n):
        # Write your code here

        patches = []
        acc = 0
        for v in nums:
            exp = acc + 1
            while exp < v:
                patches.append(exp)
                acc += exp
                exp = acc + 1
                if acc >= n:
                    break
            acc += v
            if acc >= n:
                break
        while acc < n:
            exp = acc + 1
            patches.append(exp)
            acc += exp
        return len(patches)
