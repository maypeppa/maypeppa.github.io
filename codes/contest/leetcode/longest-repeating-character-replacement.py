#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# 这道题目想复杂了，原以为是DP. 原来sliding window这么好用

from collections import Counter


def chr2int(c):
    return ord(c) - ord('A')


class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        counter = Counter()
        counter.total = 0

        def ok():
            freq = counter.most_common(1)[0][1]
            if freq + k >= counter.total:
                return True
            return False

        last = 0
        res = 0
        for (idx, c) in enumerate(s):
            counter[c] += 1
            counter.total += 1
            if ok():
                continue
            # print(last, idx - 1)
            res = max(res, idx - last)
            while last < idx:
                c2 = s[last]
                last += 1
                counter[c2] -= 1
                counter.total -= 1
                if ok():
                    break
        res = max(res, len(s) - last)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.characterReplacement('ABAB', 2))
    print(s.characterReplacement('AABABBA', 1))
    print(s.characterReplacement('AAAB', 0))
