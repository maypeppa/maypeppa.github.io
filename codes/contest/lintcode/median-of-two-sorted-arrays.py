#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """

    def findMedianSortedArrays(self, A, B):
        # write your code here

        def locate_lo(v, xs, s, e):
            # return x sat. xs[x] < v
            while s <= e:
                m = (s + e) // 2
                if xs[m] >= v:
                    e = m - 1
                else:
                    s = m + 1
            return e

        def locate_hi(v, xs, s, e):
            # return x sat. xs[x] > v
            while s <= e:
                m = (s + e) // 2
                if xs[m] <= v:
                    s = m + 1
                else:
                    e = m - 1
            return s

        def find_kth_in_A(k, A, B):
            n = len(A)
            m = len(B)
            if n == 0:
                return B[k]
            if m == 0:
                return A[k]
            s, e = 0, n - 1
            x, y = 0, m - 1
            while s <= e:
                m1 = (s + e) // 2
                v = A[m1]
                lo = locate_lo(v, B, x, y)
                hi = locate_hi(v, B, x, y)
                if (lo + 1 + m1) <= k < (hi + 1 + m1):
                    return v
                if k < (lo + 1 + m1):
                    e = m1 - 1
                    y = lo
                else:
                    s = m1 + 1
                    x = hi
            return None

        def find_kth(k, A, B):
            v = find_kth_in_A(k, A, B)
            if v is not None:
                return v
            return find_kth_in_A(k, B, A)

        n = len(A)
        m = len(B)
        k = (n + m) // 2
        if (n + m) % 2 == 1:
            return find_kth(k, A, B)
        else:
            v0 = find_kth(k - 1, A, B)
            v1 = find_kth(k, A, B)
            return (v0 + v1) * 0.5


if __name__ == '__main__':
    s = Solution()
    A = [1, 2, 4, 5]
    B = [3, 3, 3]
    print(s.findMedianSortedArrays(A, B))
