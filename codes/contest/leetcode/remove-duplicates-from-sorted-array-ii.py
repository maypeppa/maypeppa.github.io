#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        idx = 0
        prev, cnt = None, 0
        for i in range(len(nums)):
            if nums[i] == prev:
                cnt += 1
                if cnt > 2:
                    continue
            else:
                prev = nums[i]
                cnt = 1
            nums[idx] = nums[i]
            idx += 1
        return idx


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1, 1, 1, 2]))
    print(s.removeDuplicates([1]))
