#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import random


class Solution:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.n = len(nums)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """

        matched = 0
        index = 0
        for i in range(index + 1, self.n):
            if self.nums[i] == target:
                matched += 1
                if random.randint(0, matched - 1) == 0:
                    index = i
        return index
