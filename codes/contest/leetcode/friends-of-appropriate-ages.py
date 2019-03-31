#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import bisect


class Solution:
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """

        ages.sort()

        def make_range(x):
            a = (x // 2 + 7 + 1)
            b = x
            # [a, b]
            return a, b

        ans = 0
        for i in range(len(ages)):
            x = ages[i]
            a, b = make_range(x)
            if a > b: continue
            pa = bisect.bisect_left(ages, a, 0, i)
            pb = bisect.bisect_right(ages, b, 0, i)
            pc = bisect.bisect_right(ages, b, i + 1)
            # print(x, a, b, i, pa, pb, pc)
            ans += (pb - pa) + (pc - i - 1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.numFriendRequests([15, 15]))
    print(sol.numFriendRequests([16, 16]))
    print(sol.numFriendRequests([16, 17, 18]))
    print(sol.numFriendRequests([20, 30, 100, 110, 120]))
