#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from collections import Counter


class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        counter = Counter()
        for x in nums:
            counter[x] += 1

        ans = 0
        for x in nums:
            value = x
            res = 0
            while counter[value] > 0:
                res += 1
                counter[value] -= 1
                value += 1
            value = x - 1
            while counter[value] > 0:
                res += 1
                counter[value] -= 1
                value -= 1
            ans = max(ans, res)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
