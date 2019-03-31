#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        N = len(citations)
        s, e = 0, N
        ans = 0
        while s <= e:
            h = (s + e) // 2

            # valid h-index.
            c = citations[N - h] if h != 0 else 0
            c2 = citations[N - h - 1] if h != N else 0
            if c2 <= h <= c:
                ans = max(ans, h)

            if c >= h:
                s = h + 1
            else:
                e = h - 1

        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.hIndex([0, 1]))
    print(sol.hIndex([0]))
    print(sol.hIndex([1]))
