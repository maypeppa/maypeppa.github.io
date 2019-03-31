#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """

        digits = []
        while num:
            digits.append(num % 10)
            num //= 10
        digits = digits[::-1]

        n = len(digits)
        max_idx = n - 1
        swap_pair = None
        for i in reversed(range(n)):
            if digits[i] > digits[max_idx]:
                max_idx = i
            elif digits[i] < digits[max_idx]:
                swap_pair = i, max_idx

        if swap_pair:
            i, j = swap_pair
            digits[i], digits[j] = digits[j], digits[i]
        ans = 0
        for x in digits:
            ans = ans * 10 + x
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumSwap(2736))
    print(sol.maximumSwap(27376))
    print(sol.maximumSwap(9973))
