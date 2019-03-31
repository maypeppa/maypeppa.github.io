#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         cset = set()
#         (i, j, ret) = (0, 0, 0)
#         while j < len(s):
#             c = s[j]
#             while c in cset:
#                 c2 = s[i]
#                 cset.remove(c2)
#                 i += 1
#             cset.add(c)
#             ret = max(ret, len(cset))
#             j += 1
#         return ret
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = defaultdict(int)
        last = 0
        res = 0
        for (idx, c) in enumerate(s):
            counter[c] += 1
            if counter[c] == 1:
                continue
            res = max(res, idx - last)
            while last <= idx:
                c2 = s[last]
                last += 1
                counter[c2] -= 1
                if c2 == c and counter[c] == 1:
                    break
        res = max(res, len(s) - last)
        return res


if __name__ == '__main__':
    s = Solution()
    print((s.lengthOfLongestSubstring('c')))
    print((s.lengthOfLongestSubstring('')))
    print(s.lengthOfLongestSubstring("jhhthogonzpheevzetkvygpvbdhcaisjpbfwslmflbopgmqmfcjdkzbmckqeskpjluhditltvzkdlap"))
