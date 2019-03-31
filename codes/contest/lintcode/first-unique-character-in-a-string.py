#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """

    def firstUniqChar(self, str):
        # Write your code here

        counter = 0
        invalid = 0
        for c in str:
            idx = ord(c) - ord('a')
            if counter & (1 << idx):
                invalid |= (1 << idx)
            else:
                counter |= (1 << idx)
        for c in str:
            idx = ord(c) - ord('a')
            if (invalid & (1 << idx)) == 0:
                return c
        return None
