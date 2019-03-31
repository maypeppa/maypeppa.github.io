#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        dp = []
        inf = 1 << 30
        for _ in range(2):
            dp.append([inf] * m)

        now = 0
        dp[now][0] = 0

        for i in range(n):
            for j in range(m):
                prev = min(dp[now][j], dp[1 - now][j - 1] if j > 0 else inf)
                dp[1 - now][j] = (prev + grid[i][j]) if prev != inf else inf
            now = 1 - now

        return dp[now][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
