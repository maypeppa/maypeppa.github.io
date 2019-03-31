#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        INT_MIN = -(1 << 30)

        def walk(root):
            if not root:
                return INT_MIN, 0
            left_sum, left_tree = walk(root.left)
            right_sum, right_tree = walk(root.right)
            root_tree = max(left_tree, right_tree, 0) + root.val
            root_sum = max(left_sum, right_sum, max(left_tree, 0) + max(right_tree, 0) + root.val)
            return root_sum, root_tree

        res, _ = walk(root)
        return res
