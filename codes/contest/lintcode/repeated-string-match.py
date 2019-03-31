#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param A: a string
    @param B: a string
    @return: return an integer
    """

    def repeatedStringMatch(self, A, B):
        # write your code here

        n = len(A)
        m = len(B)
        repeat = (m + n - 1) // n

        C = A * repeat
        for i in range(0, n):
            if (i + len(B)) > len(C):
                C = C + A
                repeat += 1
            sc = C[i:i + len(B)]
            if sc == B:
                return repeat
        return -1
