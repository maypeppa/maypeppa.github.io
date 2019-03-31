#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: st
        :rtype: str
        """
        ss = [x for x in s.split(' ') if x]
        return ' '.join(ss[::-1])
