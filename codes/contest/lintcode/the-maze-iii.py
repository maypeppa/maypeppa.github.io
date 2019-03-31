#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# TODO(yan): TLE.

class Solution:
    """
    @param maze: the maze
    @param ball: the ball position
    @param hole: the hole position
    @return: the lexicographically smallest way
    """

    def findShortestWay(self, maze, ball, hole):
        # write your code here

        n = len(maze)
        m = len(maze[0])
        visited = [[0] * m for _ in range(n)]

        start = tuple(ball)
        destination = tuple(hole)

        left_rolls = []
        right_rolls = []
        for i in range(n):
            xs = []
            p = -1
            for j in range(m):
                xs.append(p)
                if maze[i][j] == 1:
                    p = j
            left_rolls.append(xs[::])
            xs = []
            p = m
            for j in range(m - 1, -1, -1):
                xs.append(p)
                if maze[i][j] == 1:
                    p = j
            right_rolls.append(xs[::-1])

        up_rolls = []
        down_rolls = []
        for j in range(m):
            xs = []
            p = -1
            for i in range(n):
                xs.append(p)
                if maze[i][j] == 1:
                    p = i
            up_rolls.append(xs[::])
            xs = []
            p = n
            for i in range(n - 1, -1, -1):
                xs.append(p)
                if maze[i][j] == 1:
                    p = i
            down_rolls.append(xs[::-1])

        def update(res, res_path, out, out_path):
            if out == -1:
                return res, res_path
            if res == -1:
                return out, out_path
            if res < out:
                return res, res_path
            elif res > out:
                return out, out_path
            elif res_path < out_path:
                return res, res_path
            else:
                return out, out_path

        def pass_point(x, y, p):
            if x[0] == y[0]:
                if p[0] == x[0] and min(x[1], y[1]) <= p[1] <= max(x[1], y[1]):
                    return True
                return False

            if x[1] == y[1]:
                if p[1] == x[1] and min(x[0], y[0]) <= p[0] <= max(x[0], y[0]):
                    return True
                return False

            return False

        def dfs(r, c, direction):
            visited[r][c] = 1
            next_rc = None
            if direction == 'l':  # left.
                p = left_rolls[r][c]
                next_rc = r, p + 1

            elif direction == 'r':  # right.
                p = right_rolls[r][c]
                next_rc = r, p - 1
            elif direction == 'u':  # up.
                p = up_rolls[c][r]
                next_rc = p + 1, c
            else:  # down
                p = down_rolls[c][r]
                next_rc = p - 1, c

            res = -1
            res_path = None
            if next_rc and next_rc != (r, c):
                if pass_point((r, c), next_rc, destination):
                    delta = abs(r - destination[0]) + abs(c - destination[1])
                    res, res_path = delta, direction
                else:
                    r2, c2 = next_rc
                    delta = abs(r - r2) + abs(c - c2)
                    if 0 <= r2 < n and 0 <= c2 < m and maze[r2][c2] == 0 and visited[r2][c2] == 0:
                        for d in 'dlru':
                            out, out_path = dfs(r2, c2, d)
                            if out != -1:
                                res, res_path = update(res, res_path, out + delta, direction + out_path)
            visited[r][c] = 0
            # print(r, c, direction, res)
            return res, res_path

        r, c = start
        res = -1
        res_path = None
        for d in 'dlru':
            out, out_path = dfs(r, c, d)
            res, res_path = update(res, res_path, out, out_path)
        return res_path if res_path is not None else 'impossible'


if __name__ == '__main__':
    sol = Solution()
    maze = [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]]
    start = [4, 3]
    stop = [0, 1]
    print(sol.findShortestWay(maze, start, stop))
