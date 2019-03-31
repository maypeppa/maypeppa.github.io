#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        prev = None
        k = 0
        for v in nums:
            if v == prev:
                continue
            nums[k] = v
            k += 1
            prev = v
        return k
