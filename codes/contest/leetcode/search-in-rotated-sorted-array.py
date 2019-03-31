#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        n = len(nums)
        s, e = 0, n - 1
        while s <= e:
            m = (s + e) // 2
            if nums[m] == target:
                return m
            if nums[m] >= nums[s]:
                if nums[s] <= target < nums[m]:
                    e = m - 1
                else:
                    s = m + 1
            else:
                if nums[m] < target <= nums[e]:
                    s = m + 1
                else:
                    e = m - 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search([6, 7, 1, 2, 3, 4, 5], 6))
