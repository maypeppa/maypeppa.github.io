#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []
        if root is None:
            return res

        def visit(node, depth):
            if depth >= len(res):
                assert len(res) == depth
                res.append(node.val)
            else:
                res[depth] = node.val

            if node.left:
                visit(node.left, depth + 1)
            if node.right:
                visit(node.right, depth + 1)

        visit(root, depth=0)
        return res
