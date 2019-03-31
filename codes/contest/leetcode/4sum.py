#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums.sort()
        ans = []
        n = len(nums)

        # O(n^3)
        for i in range(0, n):
            for j in range(i + 1, n):
                k, l = j + 1, n - 1
                while k < l:
                    value = nums[i] + nums[j] + nums[k] + nums[l]
                    if value == target:
                        t = (nums[i], nums[j], nums[k], nums[l])
                        ans.append(t)
                        k += 1
                    elif value > target:
                        l -= 1
                    else:
                        k += 1

        ans = [list(x) for x in set(ans)]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
