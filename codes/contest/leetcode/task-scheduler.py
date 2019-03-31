#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        cnt = [0] * 26
        for t in tasks:
            cnt[ord(t) - ord('A')] += 1

        ans = 0
        cnt.sort(key=lambda x: -x)
        while True:
            count = 0
            for i in range(26):
                if cnt[i] == 0:
                    break
                ans += 1
                cnt[i] -= 1
                count += 1
                if count == (n + 1):
                    break

            cnt.sort(key=lambda x: -x)
            if cnt[0] == 0: break
            if count < (n + 1):
                ans += (n + 1 - count)
        return ans
