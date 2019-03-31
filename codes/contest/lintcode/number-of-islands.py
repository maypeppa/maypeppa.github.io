#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n = len(grid)
        if n == 0: return 0
        m = len(grid[0])
        if m == 0: return 0
        mask = []
        for i in range(n):
            mask.append([0] * m)

        regid = 1

        def dfs(i, j):
            if grid[i][j] == 0 or mask[i][j]:
                return

            mask[i][j] = regid
            for (di, dj) in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                if (di + i) >= 0 and (di + i) < n and (dj + j) >= 0 and (dj + j) < m:
                    dfs(di + i, dj + j)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not mask[i][j]:
                    dfs(i, j)
                    regid += 1

        return regid - 1
