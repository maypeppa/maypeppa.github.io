#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def height(r):
    return r.height if r else 0


def left_rotate(root):
    # print('left_rotate!')
    left = root.left
    root.left = left.right
    root.height = max(height(root.left), height(root.right)) + 1

    left.right = root
    left.height = max(height(left.left), height(left.right)) + 1
    return left


def right_rotate(root):
    # print('right_rotate!')
    right = root.right
    root.right = right.left
    root.height = max(height(root.left), height(root.right)) + 1

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


class Span:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def overlap(self, other):
        return not (other.x >= self.y or other.y <= self.x)


class Node:
    def __init__(self, span):
        self.span = span
        self.left = None
        self.right = None
        self.height = 1


def query_and_insert(root, span):
    if root is None:
        return True, Node(span)

    if root.span.overlap(span):
        return False, root

    if span.x < root.span.x:
        ok, root.left = query_and_insert(root.left, span)
        if not ok:
            return False, root
    else:
        ok, root.right = query_and_insert(root.right, span)
        if not ok:
            return False, root
    root = balance(root)
    return True, root


class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        span = Span(start, end)
        ok, self.root = query_and_insert(self.root, span)
        return ok
