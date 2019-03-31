#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

def rand7():
    return 1


class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """

        rnd2 = None
        while True:
            rnd = rand7()
            if rnd <= 5:
                break
            else:
                rnd2 = rnd

        if rnd2 is None:
            while True:
                rnd2 = rand7()
                if rnd2 <= 6:
                    break

        res = rnd
        if rnd2 % 2 == 0:
            res += 5
        return res
