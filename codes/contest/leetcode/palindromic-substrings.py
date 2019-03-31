#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        if n == 0:
            return 0

        dp = []
        for i in range(n):
            dp.append([0] * n)
        for k in range(1, n + 1):
            for i in range(0, n - k + 1):
                j = i + k - 1
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    if (i + 1) <= (j - 1):
                        dp[i][j] = dp[i + 1][j - 1]
                    else:
                        dp[i][j] = 1

        res = 0
        for i in range(n):
            for j in range(i, n):
                if dp[i][j]:
                    # print('({}, {})'.format(i, j))
                    res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print((s.countSubstrings('aaa')))
