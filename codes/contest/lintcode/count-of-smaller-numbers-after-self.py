#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.count = 1
        self.height = 1
        self.self_count = 1


def height(r):
    return r.height if r else 0


def left_rotate(root):
    # print('left_rotate!')
    left = root.left
    root.left = left.right
    root.height = max(height(root.left), height(root.right)) + 1
    root.count -= left.count

    left.right = root
    left.height = max(height(left.left), height(left.right)) + 1
    return left


def right_rotate(root):
    # print('right_rotate!')
    right = root.right
    root.right = right.left
    root.height = max(height(root.left), height(root.right)) + 1

    right.left = root
    right.count += root.count
    right.height = max(height(right.left), height(right.right)) + 1
    return right


def balance(root):
    lh = height(root.left)
    rh = height(root.right)

    if (lh - rh) >= 2:
        llh = height(root.left.left)
        lrh = height(root.left.right)
        if lrh > llh:
            root.left = right_rotate(root.left)
        root = left_rotate(root)

    elif (rh - lh) >= 2:
        rlh = height(root.right.left)
        rrh = height(root.right.right)
        if rlh > rrh:
            root.right = left_rotate(root.right)
        root = right_rotate(root)

    else:
        root.height = max(lh, rh) + 1

    return root


def insert_value(root, value):
    if root is None:
        return Node(value)
    if root.value == value:
        root.self_count += 1
        root.count += 1
    elif root.value > value:
        root.count += 1
        root.left = insert_value(root.left, value)
    else:
        root.right = insert_value(root.right, value)
    root = balance(root)
    return root


def query_value(root, value):
    res = 0
    while root:
        if root.value == value:
            res += (root.count - root.self_count)
            break
        if root.value > value:
            root = root.left
        else:
            res += root.count
            root = root.right
    return res


class Solution:
    """
    @param nums: a list of integers
    @return: return a list of integers
    """

    def countSmaller(self, nums):
        # write your code here
        out = []
        n = len(nums)
        root = None
        for i in range(n - 1, -1, -1):
            value = nums[i]
            res = query_value(root, value)
            out.append(res)
            root = insert_value(root, value)
        return out[::-1]
