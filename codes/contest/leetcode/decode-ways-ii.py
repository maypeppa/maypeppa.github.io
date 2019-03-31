#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        def ways1(a):
            if a == '*':
                return 9
            elif a == '0':
                return 0
            return 1

        def ways(a, b):
            if b != '*':
                if a != '*':
                    if a == '0': return 0
                    val = (ord(a) - ord('0')) * 10 + (ord(b) - ord('0'))
                    if val > 26: return 0
                    return 1
                else:
                    val = ord(b) - ord('0')
                    if val <= 6:
                        return 2
                    else:
                        return 1
            else:
                if a != '*':
                    if a == '1':
                        return 9
                    elif a == '2':
                        return 6
                    else:
                        return 0
                else:
                    return 15

        if len(s) == 0: return 0
        dp = [1] * 3
        MOD = 10 ** 9 + 7
        n = len(s)
        dp[0] = ways1(s[0])
        for i in range(1, n):
            a = s[i - 1]
            b = s[i]
            val = (dp[(i + 2) % 3] * ways1(b)) + (dp[(i + 1) % 3] * ways(a, b))
            dp[i % 3] = val % MOD
        res = dp[(n - 1) % 3]
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.numDecodings('1*'))
    print(sol.numDecodings('*'))
    print(sol.numDecodings('**1**'))
    print(sol.numDecodings('*1'))
    print(sol.numDecodings("*1*1*0"))
