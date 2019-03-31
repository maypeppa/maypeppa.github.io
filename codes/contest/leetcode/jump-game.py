#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        inf = 1 << 31
        st = [inf] * len(nums)
        st[0] = 0
        for i in range(0, len(nums)):
            v = nums[i]
            # range = [i + 1, i + v]
            for j in range(min(len(nums) - 1, i + v), i, -1):
                if (st[i] + 1) < st[j]:
                    st[j] = st[i] + 1
                else:
                    # print('prune')
                    break
        return st[len(nums) - 1] != inf
