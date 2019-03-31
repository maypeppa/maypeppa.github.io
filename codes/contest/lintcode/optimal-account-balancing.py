#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


from collections import defaultdict


class Solution:
    """
    @param edges: a directed graph where each edge is represented by a tuple
    @return: the number of edges
    """

    def balanceGraph(self, edges):
        # Write your code here

        nodes = defaultdict(int)
        for (u, v, w) in edges:
            nodes[u] -= w
            nodes[v] += w

        debts = [x for x in nodes.values() if x != 0]
        # print(debts)
        n = len(debts)
        if n == 0: return 0
        dp = [-1] * (1 << n)
        for i in range(1, len(dp)):
            balance = 0
            count = 0
            for j in range(n):
                if (1 << j) & i:
                    balance += debts[j]
                    count += 1

            if balance == 0:
                exchange = count - 1
                for j in range(1, i):
                    if (i & j == j) and dp[j] != -1 and dp[i - j] != -1:
                        exchange = min(exchange, dp[j] + dp[i - j])
                dp[i] = exchange
        # print(dp)
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.balanceGraph([[0, 1, 10], [2, 0, 5]]))
    print(sol.balanceGraph([[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]))
    print(sol.balanceGraph(
        [[7, 9, 1], [9, 8, 59], [4, 0, 46], [7, 6, 92], [7, 6, 92], [2, 3, 93], [1, 3, 96], [6, 8, 70], [2, 4, 36],
         [3, 1, 23], [8, 9, 42], [8, 7, 45], [2, 4, 24], [9, 8, 17], [5, 7, 89], [0, 2, 65], [1, 0, 91], [5, 6, 2],
         [8, 9, 24], [4, 1, 41]]))
    print(sol.balanceGraph(
        [[7, 6, 1], [4, 6, 59], [8, 9, 46], [7, 5, 92], [14, 13, 92], [2, 1, 93], [9, 8, 19], [14, 13, 72], [9, 8, 68],
         [12, 16, 4], [14, 15, 74], [1, 3, 54], [3, 0, 63], [5, 7, 24], [5, 6, 17], [12, 14, 89], [8, 10, 65],
         [2, 1, 91], [6, 5, 94], [1, 3, 85], [8, 10, 77], [15, 16, 40], [11, 9, 39], [10, 9, 42], [7, 6, 5],
         [9, 10, 74], [9, 8, 73], [9, 8, 87], [9, 8, 56], [12, 16, 32], [2, 1, 25], [10, 11, 92], [14, 15, 84],
         [5, 6, 22], [2, 1, 69], [3, 2, 56], [11, 8, 38], [3, 1, 3], [11, 8, 75], [0, 1, 49]]))
