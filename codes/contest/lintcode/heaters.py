#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """

    def findRadius(self, houses, heaters):
        # Write your code here


        houses.sort()
        heaters.sort()

        def can_cover(rad):
            x, y = 0, 0
            while x < len(houses):
                if (heaters[y] - rad) <= houses[x] <= (heaters[y] + rad):
                    x += 1
                elif houses[x] < heaters[y] - rad:
                    return False
                else:
                    y += 1
                    if y == len(heaters):
                        return False
            return True

        max_rad = max(abs(houses[-1] - heaters[0]), heaters[-1] - houses[0])
        s, e = 0, max_rad
        while s <= e:
            m = (s + e) // 2
            ok = can_cover(m)
            # print(m, ok)
            if ok:
                e = m - 1
            else:
                s = m + 1
        return s
