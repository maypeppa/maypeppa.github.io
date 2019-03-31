#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import copy
import time


def sudoku_solve(grid, number=0):
    N = 9
    xs, ys, rs, ps = [], [], [], []
    for i in range(N):
        mark = [0] * (N + 1)
        for j in range(N):
            mark[grid[i][j]] = 1
        cs = 0
        for k in range(1, N + 1):
            if mark[k] == 0:
                cs |= (1 << k)
        xs.append(cs)

    for j in range(N):
        mark = [0] * (N + 1)
        for i in range(N):
            mark[grid[i][j]] = 1
        cs = 0
        for k in range(1, N + 1):
            if mark[k] == 0:
                cs |= (1 << k)
        ys.append(cs)

    for i in range(3):
        for j in range(3):
            mark = [0] * (N + 1)
            for k in range(3):
                for l in range(3):
                    v = grid[3 * i + k][3 * j + l]
                    mark[v] = 1
            cs = 0
            for k in range(1, N + 1):
                if mark[k] == 0:
                    cs |= (1 << k)
            rs.append(cs)

    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                ps.append((i, j))

    ans = []

    def dfs(idx):
        if idx == len(ps):
            ans.append(copy.deepcopy(grid))
            return

        x, y = ps[idx]
        r = (x // 3) * 3 + (y // 3)
        cs = xs[x] & ys[y] & rs[r]
        for v in range(1, 10):
            if (cs >> v) & 0x1:
                unmask = ~(1 << v)
                mask = (1 << v)
                grid[x][y] = v
                xs[x] &= unmask
                ys[y] &= unmask
                rs[r] &= unmask
                dfs(idx + 1)
                grid[x][y] = 0
                xs[x] |= mask
                ys[y] |= mask
                rs[r] |= mask
                if ans and len(ans) == number:
                    return

    dfs(0)
    return ans


def main():
    grid = [
        [7, 0, 0, 8, 3, 0, 0, 0, 5],
        [0, 2, 5, 0, 6, 0, 3, 0, 0],
        [0, 1, 0, 0, 7, 0, 9, 0, 2],
        [1, 0, 2, 5, 0, 3, 0, 7, 0],
        [5, 0, 8, 0, 0, 6, 4, 0, 0],
        [0, 3, 0, 9, 0, 0, 5, 0, 6],
        [9, 0, 6, 0, 1, 0, 0, 5, 0],
        [0, 0, 4, 0, 9, 0, 6, 1, 0],
        [3, 0, 0, 0, 5, 8, 0, 0, 4]
    ]
    # grid = [
    #     [8, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 3, 6, 0, 0, 0, 0, 0],
    #     [0, 7, 0, 0, 9, 0, 2, 0, 0],
    #     [0, 5, 0, 0, 0, 7, 0, 0, 0],
    #     [0, 0, 0, 0, 4, 0, 7, 0, 0],
    #     [0, 0, 0, 1, 0, 5, 0, 3, 0],
    #     [0, 0, 1, 0, 0, 0, 0, 6, 8],
    #     [0, 0, 8, 5, 0, 0, 0, 1, 0],
    #     [0, 9, 0, 0, 0, 0, 4, 0, 0]
    # ]
    start = time.time()
    ans = sudoku_solve(grid, number=0)
    stop = time.time()
    print('===== answer(%.2f, %s) =====' % (stop - start, len(ans)))
    for arr in ans:
        print('>' * 20)
        for i in range(len(arr)):
            print(arr[i])
        print('<' * 20)


if __name__ == '__main__':
    main()
