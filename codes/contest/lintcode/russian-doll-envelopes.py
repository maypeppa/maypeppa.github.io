#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import functools


class Solution:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """

    def maxEnvelopes(self, envelopes):
        # write your code here

        n = len(envelopes)
        if n == 0:
            return 0

        def cmp_fn(x, y):
            if x[0] != y[0]:
                if x[0] < y[0]:
                    return -1
                return 1
            if x[1] < y[1]:
                return 1
            elif x[1] > y[1]:
                return -1
            return 0

        envelopes.sort(key=functools.cmp_to_key(cmp_fn))

        # dp = [0] * n
        # dp[0] = 1
        # max_dp = 1
        # for i in range(1, n):
        #     q = envelopes[i]
        #     max_v = 0
        #     for j in range(i - 1, -1, -1):
        #         p = envelopes[j]
        #         if q[0] > p[0] and q[1] > p[1]:
        #             if dp[j] > max_v:
        #                 max_v = dp[j]
        #                 if max_v == max_dp:
        #                     break
        #     dp[i] = max_v + 1
        #     max_dp = max(max_dp, dp[i])
        # return max(dp)

        res = []

        def can_cover(p, q):
            if p[0] > q[0] and p[1] > q[1]:
                return True
            return False

        def bs(p, s, e):
            while s <= e:
                m = (s + e) // 2
                q = res[m]
                if can_cover(p, q):
                    s = m + 1
                else:
                    e = m - 1
            return s

        for i in range(n):
            p = envelopes[i]
            pos = bs(p, 0, len(res) - 1)
            if pos == len(res):
                res.append(p)
            else:
                res[pos] = p
        return len(res)
