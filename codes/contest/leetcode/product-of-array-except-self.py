#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        ans = [1] * n
        value = 1
        # left -> right
        for i in range(n):
            ans[i] *= value
            value *= nums[i]

        value = 1
        # right -> left
        for i in range(n - 1, -1, -1):
            ans[i] *= value
            value *= nums[i]

        return ans


if __name__ == '__main__':
    s = Solution()
    print((s.productExceptSelf([1, 2, 3, 4])))
