#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# class Solution(object):
#     def minWindow(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#
#         from collections import defaultdict
#         dt = defaultdict(int)
#         for c in t: dt[c] += 1
#         d = defaultdict(int)
#
#         def cover():
#             for k in dt.keys():
#                 if d[k] < dt[k]:
#                     return False
#             return True
#
#         min_len = 1 << 31
#         min_range = (0, 0)
#         j = 0
#         for i in range(0, len(s)):
#             c = s[i]
#             if c not in dt:
#                 continue
#             d[c] += 1
#             while cover():
#                 # print d, dt, i, j
#                 if (i - j + 1) < min_len:
#                     min_len = i - j + 1
#                     min_range = (j, i)
#                 d[s[j]] -= 1
#                 j += 1
#                 while j <= i and s[j] not in dt: j += 1
#
#         if min_len == 1 << 31: return ''
#         return s[min_range[0]: min_range[1] + 1]

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        from collections import defaultdict
        dt = defaultdict(int)
        for c in t:
            dt[c] += 1
        counter = len(t)

        min_interval = 1 << 31
        min_range = None

        begin, end = 0, 0,
        while end < len(s):
            c = s[end]
            end += 1
            dt[c] -= 1
            if dt[c] >= 0:
                counter -= 1
            if counter > 0:
                continue

            while counter == 0:
                interval = (end - begin)
                if interval < min_interval:
                    min_interval = interval
                    min_range = (begin, end - 1)
                c = s[begin]
                begin += 1
                dt[c] += 1
                if dt[c] >= 1:
                    counter += 1

        if min_range is None:
            return ''
        return s[min_range[0]:min_range[1] + 1]


if __name__ == '__main__':
    s = Solution()
    print((s.minWindow('ADOBECODEBANC', 'ABC')))
    print((s.minWindow("bba", "ab")))
    print((s.minWindow("aa", "aa")))
