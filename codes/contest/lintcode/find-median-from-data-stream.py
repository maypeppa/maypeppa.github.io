#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from queue import PriorityQueue


class MinQItem:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value


class MaxQItem:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value


def peek(q):
    return q.queue[0]


class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """

    def medianII(self, nums):
        # write your code here
        leftq = PriorityQueue()
        rightq = PriorityQueue()

        def add_and_query(value):
            if leftq.qsize() == 0:
                leftq.put(MaxQItem(value))
            else:
                x = peek(leftq)
                if value <= x.value:
                    leftq.put(MaxQItem(value))
                else:
                    rightq.put(MinQItem(value))

            # balance them.
            if (rightq.qsize() - leftq.qsize()) == 1:
                x = rightq.get()
                x = MaxQItem(x.value)
                leftq.put(x)
            elif (leftq.qsize() - rightq.qsize()) == 2:
                x = leftq.get()
                x = MinQItem(x.value)
                rightq.put(x)

            x = peek(leftq)
            return x.value

        res = []
        for value in nums:
            out = add_and_query(value)
            res.append(out)
        return res
