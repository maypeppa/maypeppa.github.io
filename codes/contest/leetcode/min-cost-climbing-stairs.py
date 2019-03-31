#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        inf = 1 << 20
        n = len(cost)
        dp = [inf] * (n + 1)
        dp[0], dp[1] = 0, 0
        for i in range(n):
            for step in (1, 2):
                j = i + step
                if j < (n + 1):
                    dp[j] = min(dp[j], dp[i] + cost[i])
        return dp[n]
