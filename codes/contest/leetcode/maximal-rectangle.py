#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# class Solution(object):
#     def maximalRectangle(self, matrix):
#         """
#         :type matrix: List[List[str]]
#         :rtype: int
#         """
#         n = len(matrix)
#         if n == 0: return 0
#         m = len(matrix[0])
#         if m == 0: return 0
#
#         # O(n^2 * m), 枚举所有的row pairs.
#         # 对于(rx, ry), column mth. 如果m列rx行到ry行均为1的话
#         # 则认为1，否则认为0. 这样变为找到最长连续1的区间.
#         # csum[m][ry+1] - csum[m][rx] == (ry - rx + 1)来快速判断.
#
#         csum = []
#         for i in range(m):
#             csum.append([0] * (n + 1))
#
#         for i in range(m):
#             csum[i][0] = 0
#             for j in range(n):
#                 csum[i][j + 1] = csum[i][j] + int(matrix[j][i])
#
#         # print csum
#         def f(rx, ry):
#             cnt = 0
#             res = 0
#             for i in range(m):
#                 v = csum[i][ry + 1] - csum[i][rx]
#                 if v == (ry - rx + 1):
#                     cnt += 1
#                     res = max(res, cnt)
#                 else:
#                     cnt = 0
#             return res * (ry - rx + 1)
#
#         res = 0
#         for i in range(n):
#             for j in range(i, n):
#                 res = max(res, f(i, j))
#         return res

# O(nm)的DP算法
# https://leetcode.com/problems/maximal-rectangle/discuss/29054/Share-my-DP-solution
# left[i] = j 表示 对于所有k in [j..i], height[k]>=height[i],
# right[i] =j 表示 对于所有k in [i..j], height[k]>=height[i]
# 所以最大尺寸应该是(right[i] - left[i]+1) * height[i]

class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n = len(matrix)
        if n == 0: return 0
        m = len(matrix[0])
        if m == 0: return 0
        height = [0] * m
        left = [0] * m
        right = [m - 1] * m

        ans = 0
        # print('===== matrix =====')
        # for i in range(n):
        #     print(matrix[i])

        for i in range(n):
            L, R = 0, m - 1
            for j in reversed(range(m)):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], R)
                else:
                    right[j] = m - 1
                    R = j - 1

            for j in range(m):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], L)
                    height[j] += 1
                    ans = max(ans, (right[j] - left[j] + 1) * height[j])
                else:
                    left[j] = 0
                    height[j] = 0
                    L = j + 1
                    # print(left, right, height, ans)
        return ans


# 另外一种办法是将它转成largest rectangle in histogram.
# https://leetcode.com/problems/maximal-rectangle/discuss/165472/Largest-Rectangle-Python

if __name__ == '__main__':
    s = Solution()

    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print(s.maximalRectangle(matrix))
    print(s.maximalRectangle([["1"]]))
