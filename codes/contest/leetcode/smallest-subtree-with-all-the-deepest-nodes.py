#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def solve(root, depth):
            # print(root, depth)

            if root.left and root.right:
                l, ld = solve(root.left, depth + 1)
                r, rd = solve(root.right, depth + 1)
                # print(root.val, l.val, r.val, ld, rd)
                if ld == rd:
                    res = root, ld
                elif ld > rd:
                    res = l, ld
                else:
                    res = r, rd

            elif root.left:
                l, ld = solve(root.left, depth + 1)
                res = l, ld

            elif root.right:
                r, rd = solve(root.right, depth + 1)
                res = r, rd

            else:
                res = root, depth

            return res

        if root is None: return None
        h, _ = solve(root, 1)
        return h


def list_to_tree(xs):
    stack = []
    root = TreeNode(xs[0])
    stack.append(root)
    i = 1
    while i < len(xs):
        h = stack.pop(0)
        if xs[i]:
            l = TreeNode(xs[i])
            h.left = l
            stack.append(l)
        i += 1

        if i < len(xs):
            if xs[i]:
                r = TreeNode(xs[i])
                h.right = r
                stack.append(r)
            i += 1
    return root


if __name__ == '__main__':
    s = Solution()
    print(s.subtreeWithAllDeepest(list_to_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])))
