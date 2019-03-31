#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param matrix: an integer matrix
    @return: the length of the longest increasing path
    """

    def longestIncreasingPath(self, matrix):
        # write your code here

        n = len(matrix)
        if n == 0: return 0
        m = len(matrix[0])
        if m == 0: return 0

        dp = []
        for _ in range(n):
            dp.append([0] * m)

        def dfs(r, c):
            if dp[r][c]:
                return dp[r][c]
            dist = 0
            for dx, dy in ((0, 1), (0, -1), (-1, 0), (1, 0)):
                r2, c2 = r + dx, c + dy
                if 0 <= r2 < n and 0 <= c2 < m and matrix[r2][c2] > matrix[r][c]:
                    dist = max(dist, dfs(r2, c2))
            dist += 1
            dp[r][c] = dist
            return dist

        res = 0
        for r in range(n):
            for c in range(m):
                dist = dfs(r, c)
                res = max(res, dist)
        return res
