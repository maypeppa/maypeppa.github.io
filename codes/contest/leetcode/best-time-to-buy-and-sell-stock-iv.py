#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    # TLE. O(n^2 * k)
    def maxProfit1(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

        n = len(prices)
        cache = {}

        def dfs(i, k):
            if i >= n: return 0
            if k == 0: return 0

            key = '{}.{}'.format(i, k)
            if key in cache:
                return cache[key]

            ans = 0
            for x in range(i, n):
                for y in range(x + 1, n):
                    ans = max(ans, max(prices[y] - prices[x], 0) + dfs(y + 1, k - 1))

            cache[key] = ans
            return ans

        ans = dfs(0, k)
        return ans

    # TLE. O(n^2 * k)
    def maxProfit2(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

        n = len(prices)
        if n == 0: return 0

        # dp[i][j] 观察到位置i, 做过j次交易的max_profit.
        dp = [[0] * (k + 1) for _ in range(n)]

        # 下面是两种不同的迭代方法，最外层迭代是O(n)

        # for i in range(n):
        #     min_value = prices[i]
        #     dp[i][0] = 0
        #     for j in reversed(range(i + 1)):
        #         min_value = min(prices[j], min_value)
        #         for d in range(1, k + 1):
        #             dp[i][d] = max(dp[i][d], dp[j][d - 1] + prices[i] - min_value)

        for i in range(n):
            dp[i][0] = 0
            for d in range(1, k + 1):
                max_cost = -prices[i]
                min_value = prices[i]
                for j in reversed(range(i + 1)):
                    min_value = min(prices[j], min_value)
                    max_cost = max(dp[j][d - 1] - min_value, max_cost)
                max_cost += prices[i]
                dp[i][d] = max_cost

        # for i in range(n):
        #     print(dp[i])
        ans = max((max(x) for x in dp))
        return ans

    # TLE. O(n^2 * k). 和maxProfit2类似，但是最外层是O(k)迭代
    def maxProfit3(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

        n = len(prices)
        if n == 0: return 0

        dp = [[0] * n for _ in range(k + 1)]
        for d in range(k):
            for i in range(n):
                min_price = prices[i]
                max_profit = 0
                for j in reversed(range(i + 1)):
                    min_price = min(min_price, prices[j])
                    max_profit = max(max_profit, dp[d][j] + prices[i] - min_price)
                dp[d + 1][i] = max_profit

        # for i in range(n):
        #     print(dp[i])q
        ans = max((max(x) for x in dp))
        return ans

    def maxProfit(self, k, prices):
        a = self.maxProfit1(k, prices)
        b = self.maxProfit2(k, prices)
        c = self.maxProfit3(k, prices)
        return a, b, c


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit(2, [2, 4, 1]))
    print(sol.maxProfit(2, [3, 2, 6, 5, 0, 3]))
    print(sol.maxProfit(2, [3, 3, 5, 0, 0, 3, 1, 4]))
    print(sol.maxProfit(2, [2, 1, 4, 5, 2, 9, 7]))
    print(sol.maxProfit(2, [2, 1, 2, 1, 0, 0, 1]))
