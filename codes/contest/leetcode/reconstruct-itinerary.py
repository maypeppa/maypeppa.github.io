#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        cities = {}
        cs = []
        for (f, t) in tickets:
            if f not in cities:
                cities[f] = len(cs)
                cs.append(f)
            if t not in cities:
                cities[t] = len(cs)
                cs.append(t)
        n = len(cs)
        adj = [[] for _ in range(n)]
        for idx, (f, t) in enumerate(tickets):
            adj[cities[f]].append((idx, cities[t]))
        for u in range(n):
            adj[u].sort(key=lambda x: cs[x[1]])

        ans = []
        edges = [0] * len(tickets)

        def dfs(u):
            if len(ans) == len(tickets) + 1:
                return True

            for edge_idx, v in adj[u]:
                if edges[edge_idx] == 0:
                    ans.append(v)
                    edges[edge_idx] = 1
                    if dfs(v):
                        return True
                    edges[edge_idx] = 0
                    ans.pop()
            return False

        src = cities['JFK']
        ans.append(src)
        dfs(src)
        ans = [cs[i] for i in ans]
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
    print(sol.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
    print(sol.findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]))
