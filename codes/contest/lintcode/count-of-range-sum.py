#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.lenum = 1
        self.height = 1


def height(r):
    return r.height if r else 0


def lenum(r):
    return r.lenum if r else 0


def left_rotate(root):
    # print('left_rotate!')
    left = root.left
    root.left = left.right
    root.lenum = root.lenum - lenum(left)
    root.height = max(height(root.left), height(root.right)) + 1

    left.right = root
    left.height = max(height(left.left), height(left.right)) + 1
    return left


def right_rotate(root):
    # print('right_rotate!')
    right = root.right
    root.right = right.left
    root.height = max(height(root.left), height(root.right)) + 1

    right.lenum = right.lenum + lenum(root)
    right.left = root
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


def insert(root, value, do_balance):
    if root is None:
        return Node(value)

    if root.value == value:
        root.lenum += 1
    elif root.value > value:
        root.left = insert(root.left, value, do_balance)
        root.lenum += 1
    else:
        root.right = insert(root.right, value, do_balance)
    if do_balance:
        root = balance(root)
    return root


def query(root, value):
    if root is None:
        return 0

    if root.value == value:
        return root.lenum
    elif root.value > value:
        return query(root.left, value)
    else:
        count = query(root.right, value)
        count += root.lenum
        return count


class Tree:
    def __init__(self, do_balance=True):
        self.root = None
        self.do_balance = do_balance

    def height(self):
        return height(self.root)

    def insert_value(self, value):
        self.root = insert(self.root, value, do_balance=self.do_balance)

    def query_value(self, value):
        return query(self.root, value)


class Solution:
    """
    @param nums: a list of integers
    @param lower: a integer
    @param upper: a integer
    @return: return a integer
    """

    def countRangeSum(self, nums, lower, upper):
        # write your code here
        tree = Tree()
        # dtree = Tree(do_balance=False)
        acc = 0
        res = 0
        for num in nums:
            # print(tree.height())
            acc += num
            lo = tree.query_value(acc - upper - 1)
            hi = tree.query_value(acc - lower)

            # dlo = dtree.query_value(acc - upper - 1)
            # dhi = dtree.query_value(acc - lower)
            # if dlo != lo or dhi != hi:
            #     print('mismatch!!')

            res += (hi - lo)
            # print('{} {} {} {}'.format(acc - upper - 1, acc - lower, lo, hi))
            tree.insert_value(acc)
            # dtree.insert_value(acc)
            if lower <= acc <= upper:
                res += 1
        return res
