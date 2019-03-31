#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import Counter


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: a root of integer
    @return: return a integer
    """

    def findMode(self, root):
        # write your code here

        def walk(root):
            if root is None:
                return Counter()
            ld = walk(root.left)
            rd = walk(root.right)
            ld.update(rd)
            ld[root.val] += 1
            return ld

        d = walk(root)
        max_occ = max(d.values())
        res = [x[0] for x in d.items() if x[1] == max_occ]
        res.sort()
        return res
