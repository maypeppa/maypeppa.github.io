#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """

    def isMatch(self, s, p):
        # write your code here

        cache = {}

        def match(si, pi):
            if si == -1 and pi == -1:
                return True
            if si == -1:
                for x in range(0, pi + 1):
                    if p[x] != '*':
                        return False
                return True
            if si == -1 or pi == -1:
                return False
            key = '{}.{}'.format(si, pi)
            if key in cache:
                return cache[key]
            if p[pi] == '*':
                ok = False
                for si2 in range(si, -2, -1):
                    ok = match(si2, pi - 1)
                    if ok:
                        break
            elif p[pi] == '?':
                ok = match(si - 1, pi - 1)
            else:
                ok = (s[si] == p[pi] and match(si - 1, pi - 1))
            cache[key] = ok
            return ok

        return match(len(s) - 1, len(p) - 1)
