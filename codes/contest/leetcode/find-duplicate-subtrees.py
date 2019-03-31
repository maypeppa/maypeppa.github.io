#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# TODO(yan): WA.

# Definition for a binary tree node.
from collections import defaultdict


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """

        id_allocator = defaultdict(int)
        collect = defaultdict(int)

        res = []

        def walk(root):
            if root is None: return 0
            left_id = walk(root.left)
            right_id = walk(root.right)
            serial = '{},{},{}'.format(root.val, left_id, right_id)
            if serial not in id_allocator:
                id_counter = len(id_allocator) + 1
                id_allocator[serial] = id_counter
            id_counter = id_allocator[serial]
            collect[id_counter] += 1
            if collect.get(id_counter) == 2:
                res.append(root)
            return serial

        walk(root)
        return res
