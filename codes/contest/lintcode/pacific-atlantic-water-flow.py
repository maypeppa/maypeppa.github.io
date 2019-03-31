#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param matrix: the given matrix
    @return: The list of grid coordinates
    """

    def pacificAtlantic(self, matrix):
        # write your code here

        n = len(matrix)
        if n == 0: return 0
        m = len(matrix[0])
        if m == 0: return 0

        nm = n * m

        def dfs(r, c, rs):
            if (r, c) in rs:
                return
            rs.add((r, c))
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                r2 = r + dr
                c2 = c + dc
                if 0 <= r2 < n and 0 <= c2 < m and matrix[r2][c2] >= matrix[r][c]:
                    dfs(r2, c2, rs)
            return

        pacs = set()
        for i in range(m):
            dfs(0, i, pacs)
        for i in range(1, n):
            dfs(i, 0, pacs)
        atls = set()
        for i in range(m):
            dfs(n - 1, i, atls)
        for i in range(0, n - 1):
            dfs(i, m - 1, atls)
        res = list(pacs & atls)
        res.sort()
        return res
