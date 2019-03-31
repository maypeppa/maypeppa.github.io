#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        def encode(s):
            st = [0] * 26
            for c in s:
                st[ord(c) - ord('a')] += 1
            return st

        if len(s2) < len(s1):
            return False

        st1 = encode(s1)
        st2 = encode(s2[:len(s1)])
        if st1 == st2:
            return True

        i = len(s1)
        while i < len(s2):
            in_ch = s2[i]
            out_ch = s2[i - len(s1)]
            st2[ord(out_ch) - ord('a')] -= 1
            st2[ord(in_ch) - ord('a')] += 1
            if st1 == st2:
                return True
            i += 1
        return False
