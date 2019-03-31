#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """

        # n = len(ratings)
        # ss = [1] * n
        # while True:
        #     changed = False
        #     for i in range(n):
        #         L = i - 1
        #         R = i + 1
        #         if L >= 0 and ratings[i] > ratings[L] and ss[i] <= ss[L]:
        #             ss[i] = ss[L] + 1
        #             changed = True
        #         if R < n and ratings[i] > ratings[R] and ss[i] <= ss[R]:
        #             ss[i] = ss[R] + 1
        #             changed = True
        #     if not changed:
        #         break
        # # print ss
        # return sum(ss)

        def L2R(ratings):
            n = len(ratings)
            ss = [1] * n
            i = 0
            while i < n:
                s = i
                while (s + 1) < n and ratings[s] > ratings[s + 1]:
                    s += 1
                v = 1
                for j in range(s, i - 1, -1):
                    ss[j] = v
                    v += 1
                i = s + 1
            return ss

        ss1 = L2R(ratings)
        ss2 = L2R(ratings[::-1])[::-1]
        ss = list(zip(ss1, ss2))
        ss = [max(x[0], x[1]) for x in ss]
        # return ss
        return sum(ss)


if __name__ == '__main__':
    s = Solution()
    print(s.candy([1, 2]))
    print(s.candy([1, 2, 2]))
