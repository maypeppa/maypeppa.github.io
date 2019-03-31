#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        if k == 0: return num

        xs = [ord(x) - ord('0') for x in num]
        st = []

        i = 0
        while i < len(xs):
            while st and xs[i] < st[-1]:
                st.pop()
                k -= 1
                if k == 0:
                    break
            if k == 0:
                break
            st.append(xs[i])
            i += 1
        st.extend(xs[i:])

        if k:
            st = st[:-k]

        i = 0
        while i < len(st) and st[i] == 0:
            i += 1
        st = st[i:]
        if not st: return '0'
        return ''.join([chr(x + ord('0')) for x in st])


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeKdigits('1432219', 3))
    print(sol.removeKdigits('1432219', 2))
    print(sol.removeKdigits('10200', 1))
    print(sol.removeKdigits('2', 2))

