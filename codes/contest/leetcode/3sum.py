#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         nums.sort()
#         n = len(nums)
#         ans = []
#         dedup = set()
#
#         for i in range(n):
#             target = 0 - nums[i]
#             j, k = i + 1, n - 1
#             while j < k:
#                 value = nums[j] + nums[k]
#                 if value == target:
#                     a, b, c = nums[i], nums[j], nums[k]
#                     value = (a, b, c)
#                     if value not in dedup:
#                         ans.append(value)
#                         dedup.add(value)
#                     j += 1
#                 elif value > target:
#                     k -= 1
#                 else:
#                     j += 1
#         return ans

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: continue

            target = 0 - nums[i]
            j, k = i + 1, n - 1
            while j < k:
                value = nums[j] + nums[k]
                if value == target:
                    a, b, c = nums[i], nums[j], nums[k]
                    value = (a, b, c)
                    ans.append(value)
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif value > target:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                else:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
    print(s.threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))
    print(s.threeSum([0] * 512))
