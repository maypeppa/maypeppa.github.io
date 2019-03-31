#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from collections import defaultdict


def chr2int(c):
    return ord(c) - ord('a')


def make_ft(s):
    ft = [0] * 26
    for c in s:
        ci = chr2int(c)
        ft[ci] += 1
    return tuple(ft)


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        groups = defaultdict(list)
        for s in strs:
            ft = make_ft(s)
            groups[ft].append(s)

        res = []
        for v in groups.values():
            res.append(v)
        return res
