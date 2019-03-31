#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """

        def make(r0, c0, r1, c1):
            val = None
            leaf = True
            for r in range(r0, r1 + 1):
                for c in range(c0, c1 + 1):
                    if val is None:
                        val = grid[r][c]
                    elif grid[r][c] != val:
                        leaf = False
                        break
                if not leaf: break
            if leaf:
                return Node(val, leaf, None, None, None, None)

            size = (r1 - r0 + 1)
            step = size // 2
            top_left = make(r0, c0, r0 + step - 1, c0 + step - 1)
            top_right = make(r0, c0 + step, r0 + step - 1, c1)
            bottom_left = make(r0 + step, c0, r1, c0 + step - 1)
            bottom_right = make(r0 + step, c0 + step, r1, c1)
            return Node(True, False, top_left, top_right, bottom_left, bottom_right)

        n = len(grid)
        return make(0, 0, n - 1, n - 1)


if __name__ == '__main__':
    sol = Solution()
    grid = [[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]]
    print(sol.construct(grid))
