"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.
"""

from typing import List
from collections import deque


# BSF version
class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        res = 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1":
                    q = deque()
                    q.append((x, y))
                    while q:
                        c, d = q.popleft()
                        cases = (
                            (c + 1, d),
                            (c - 1, d),
                            (c, d + 1),
                            (c, d - 1),
                        )
                        grid[c][d] = "2"

                        for a, b in cases:
                            if a < 0 or b < 0 or a >= rows or b >= cols:
                                continue

                            if grid[a][b] == "1":
                                q.append((a, b))
                                grid[a][b] = "2"

                    res += 1
        return res


# DFS version
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return

            if grid[r][c] != "1":
                return

            grid[r][c] = "2"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        res = 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1":
                    res += 1
                    dfs(x, y)
        return res


if __name__ == "__main__":
    s = Solution()
    assert (
        s.numIslands(
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        )
        == 1
    )
    assert s.numIslands([["1", "0", "1", "1", "0", "1", "1"]]) == 3
