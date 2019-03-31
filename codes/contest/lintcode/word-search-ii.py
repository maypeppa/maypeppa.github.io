#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Trie:
    def __init__(self, ch=None):
        self.ch = ch
        self.nxts = [None] * 26
        self.eof = False
        self.eifx = -1

    def insert(self, chs, eidx):
        root = self
        idx = 0
        while idx < len(chs):
            ch = chs[idx]
            idx += 1
            if root.nxts[ch] is None:
                node = Trie(ch)
                root.nxts[ch] = node
            root = root.nxts[ch]
        root.eof = True
        root.eidx = eidx


class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """

    def wordSearchII(self, board, words):
        # write your code here

        trie = Trie()
        for idx in range(0, len(words)):
            w = words[idx]
            chs = [ord(x) - ord('a') for x in w]
            trie.insert(chs, idx)

        res = []
        n = len(board)
        if n == 0: return res
        m = len(board[0])
        if m == 0: return res
        nm = n * m
        vis = [0] * nm

        def dfs(r, c, node):
            if node is None:
                return
            if node.eof:
                res.append(node.eidx)
            vis[r * m + c] = 1
            ch = ord(board[r][c]) - ord('a')
            assert node.ch == ch
            for dr, dc in ((0, 1), (0, -1), (-1, 0), (1, 0)):
                r2 = r + dr
                c2 = c + dc
                if 0 <= r2 < n and 0 <= c2 < m and vis[r2 * m + c2] == 0:
                    ch2 = ord(board[r2][c2]) - ord('a')
                    node2 = node.nxts[ch2]
                    dfs(r2, c2, node2)
            vis[r * m + c] = 0

        for r in range(n):
            for c in range(m):
                ch = ord(board[r][c]) - ord('a')
                node = trie.nxts[ch]
                dfs(r, c, node)

        res = list(set(res))
        res = [words[x] for x in res]
        return res
