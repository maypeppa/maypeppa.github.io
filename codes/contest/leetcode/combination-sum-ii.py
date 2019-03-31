#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# class Solution(object):
#     def combinationSum2(self, candidates, target):
#         """
#         :type candidates: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         candidates = list([x for x in candidates if x <= target])
#         if not candidates: return []
#
#         candidates.sort()
#         st = []
#         for i in range(len(candidates)):
#             sub_st = []
#             for j in range(0, target + 1):
#                 sub_st.append([])
#             st.append(sub_st)
#
#         a = candidates[0]
#         st[0][a].append([a])
#         st[0][0].append([])
#
#         for i in range(1, len(candidates)):
#             a = candidates[i]
#             for t in range(0, target + 1):
#                 if not st[i - 1][t]: continue
#                 possibles = st[i - 1][t]
#                 st[i][t].extend(st[i - 1][t][:])
#                 if (t + a) <= target:
#                     for p in possibles:
#                         st[i][t + a].append(p + [a])
#
#         res = st[len(candidates) - 1][target]
#         res = list(map(list, set(map(tuple, res))))
#         return res


class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        cache = {}
        candidates.sort()

        def solve(idx, target):
            if target == 0:
                return [[]]
            if idx < 0:
                return []
            cache_key = '{}.{}'.format(idx, target)
            if cache_key in cache:
                return cache[cache_key]
            res = []
            next_idx = idx - 1
            while next_idx >= 0 and candidates[next_idx] == candidates[idx]:
                next_idx -= 1

            if candidates[idx] <= target:
                xs = solve(idx - 1, target - candidates[idx])
                for x in xs:
                    res.append(x + [candidates[idx]])
            xs = solve(next_idx, target)
            res.extend(xs)
            cache[cache_key] = res
            return res

        res = solve(len(candidates) - 1, target)
        return res


if __name__ == '__main__':
    s = Solution()
    print((s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)))
