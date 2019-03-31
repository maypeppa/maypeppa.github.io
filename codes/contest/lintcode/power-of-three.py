#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param n: an integer
    @return: if n is a power of three
    """

    def isPowerOfThree(self, n):
        # Write your code here

        max_value = 3 ** 31
        return max_value % n == 0
