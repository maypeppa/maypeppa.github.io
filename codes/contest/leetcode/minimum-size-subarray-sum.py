#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import bisect


class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        if n == 0: return 0

        acc = [0] * (n + 1)
        ans = n + 1
        for i in range(n):
            acc[i + 1] = acc[i] + nums[i]
            exp = acc[i + 1] - s
            idx = bisect.bisect_right(acc, exp, 0, i + 1)
            # print(acc[:i], exp, idx, i)

            # acc[idx..] > exp, acc[..idx] <= exp
            # so acc[idx-1] <= exp definitely
            # which means nums[idx-1] + ... nums[i] >= s
            if idx <= 0:
                continue
            ans = min(ans, i - idx + 2)
        return ans if ans != (n + 1) else 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
    print(sol.minSubArrayLen(4, [1, 4, 4]))
    print(sol.minSubArrayLen(15, [1, 2, 3, 4, 5]))
