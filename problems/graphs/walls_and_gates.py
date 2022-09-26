"""
https://www.lintcode.com/problem/663/

You are given a m x n 2D grid initialized with these three possible values.
-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647. Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF

After running your function, the 2D grid should be:
 3  -1   0   1
 2   2   1  -1
 1  -1   2  -1
 0  -1   3   4
"""

from typing import List
from math import inf
from collections import deque


class Solution:
    def walls_and_gates(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        def add_room(row, col, res):
            if (
                row < 0
                or col < 0
                or row >= m
                or col >= n
                or (row, col) in seen
                or grid[row][col] == -1
            ):
                return

            seen.add((row, col))
            q.append((row, col))
            grid[row][col] = res

        seen = set()
        q = deque()
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 0:
                    add_room(x, y, 0)
                    q.append((x, y))
                    seen.add((x, y))

        res = 1
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                add_room(x + 1, y, res)
                add_room(x - 1, y, res)
                add_room(x, y + 1, res)
                add_room(x, y - 1, res)

            res += 1
        return grid


if __name__ == "__main__":
    s = Solution()
    grid = [
        [inf, -1, 0, inf],
        [inf, inf, inf, -1],
        [inf, -1, inf, -1],
        [0, -1, inf, inf],
    ]
    ans = [
        [3, -1, 0, 1],
        [2, 2, 1, -1],
        [1, -1, 2, -1],
        [0, -1, 3, 4],
    ]
    assert s.walls_and_gates(grid) == ans
