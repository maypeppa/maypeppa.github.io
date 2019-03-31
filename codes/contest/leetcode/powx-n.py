#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        y = 1
        b = x
        invert = (n < 0)
        n = abs(n)
        while n:
            if n & 1:
                y = y * b
            n = n >> 1
            b = b * b
        if invert: y = 1.0 / y
        return y


if __name__ == '__main__':
    s = Solution()
    print(s.myPow(5.0, 5))
    print(s.myPow(5.0, -5))
