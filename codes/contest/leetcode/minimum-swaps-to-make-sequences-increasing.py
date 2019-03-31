#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """

        dp = [[0, 0], [0, 0]]
        n = len(A)
        sw = 0
        INT_MAX = 1 << 30
        dp[sw][0] = 0
        dp[sw][1] = 1
        for i in range(1, n):
            dp[1 - sw][0] = INT_MAX
            dp[1 - sw][1] = INT_MAX

            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                dp[1 - sw][0] = min(dp[sw][0], dp[1 - sw][0])
                dp[1 - sw][1] = min(dp[sw][1] + 1, dp[1 - sw][1])

            if B[i] > A[i - 1] and A[i] > B[i - 1]:
                dp[1 - sw][0] = min(dp[sw][1], dp[1 - sw][0])
                dp[1 - sw][1] = min(dp[sw][0] + 1, dp[1 - sw][1])

            sw = 1 - sw
        return min(dp[sw])
