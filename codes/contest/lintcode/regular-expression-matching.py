#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param s: A string
    @param p: A string includes "." and "*"
    @return: A boolean
    """

    def isMatch(self, s, p):
        # write your code here
        n = len(s)
        m = len(p)

        cache = {}

        def ch_match(a, b):
            if a == '.': return True
            return a == b

        def try_match(sidx, pidx):
            if sidx == -1 and pidx == -1:
                return True
            if pidx == -1:
                return False

            cache_key = '{}.{}'.format(sidx, pidx)
            if cache_key in cache:
                return cache[cache_key]

            # special case.
            if sidx == -1:
                ok = True
                while pidx >= 0:
                    if p[pidx] == '*' and pidx >= 1:
                        pidx -= 2
                    else:
                        ok = False
                        break
                cache[cache_key] = ok
                return ok

            # general match.
            ok = False
            if p[pidx] == '*':
                if pidx >= 1:
                    c = p[pidx - 1]
                    ok = try_match(sidx, pidx - 2)
                    if not ok:
                        for i in range(sidx, -1, -1):
                            if not ch_match(c, s[i]):
                                break
                            if try_match(i - 1, pidx - 2):
                                ok = True
                                break
            else:
                ok = ch_match(p[pidx], s[sidx]) and try_match(sidx - 1, pidx - 1)
            cache[cache_key] = ok
            return ok

        return try_match(n - 1, m - 1)


if __name__ == '__main__':
    sol = Solution()
    s = 'acaabbaccbbacaabbbb'
    p = 'a*.*b*.*a*aa*a*'
    print(sol.isMatch(s, p))
    s = "aaaab"
    p = "c*a*b"
    print(sol.isMatch(s, p))
    s = 'abcde'
    p = '......'
    print(sol.isMatch(s, p))
    s = 'lintcode'
    p = '*'
    print(sol.isMatch(s, p))
