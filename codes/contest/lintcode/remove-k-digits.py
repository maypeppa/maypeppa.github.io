#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param num: a string
    @param k: an integer
    @return: return a string
    """

    def removeKdigits(self, num, k):
        # write your code here

        if k == 0: return num
        cuts = 0
        saved = []
        idx = 0

        while idx < len(num):
            v = num[idx]
            if not saved:
                saved.append(v)
                idx += 1
                continue
            while saved and v < saved[-1]:
                saved.pop()
                cuts += 1
                if cuts == k:
                    break
            if cuts == k:
                break
            saved.append(v)
            idx += 1

        res = ''.join(saved) + num[idx:]
        if cuts < k:
            res = res[:-(k - cuts)]
        idx = 0
        while idx < len(res) and res[idx] == '0':
            idx += 1
        res = res[idx:]
        if res == '':
            res = '0'
        return res
