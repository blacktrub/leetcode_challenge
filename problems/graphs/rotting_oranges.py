"""
You are given an m x n grid where each cell can have one of three values:
    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 10
    grid[i][j] is 0, 1, or 2.
"""

from typing import List


from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def mark_neighbour(r, c, q):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return 0

            if grid[r][c] != 1:
                return 0

            grid[r][c] = 2
            q.append((r, c))
            return 1

        fresh, rotten = 0, 0
        q = deque()
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    fresh += 1
                if grid[x][y] == 2:
                    q.append((x, y))
                    rotten += 1

        if not fresh:
            return 0

        res = 0
        while fresh > 0 and q:
            if not q:
                return -1

            prev = rotten
            for _ in range(len(q)):
                row, col = q.popleft()
                step = 0
                step += mark_neighbour(row + 1, col, q)
                step += mark_neighbour(row - 1, col, q)
                step += mark_neighbour(row, col + 1, q)
                step += mark_neighbour(row, col - 1, q)
                fresh -= step
                rotten += step

            if rotten == prev:
                return -1

            res += 1

        return res if fresh == 0 else -1


if __name__ == "__main__":
    s = Solution()
    assert (
        s.orangesRotting(
            [
                [2, 1, 1],
                [1, 1, 0],
                [0, 0, 1],
            ]
        )
        == -1
    )
    assert (
        s.orangesRotting(
            [
                [2, 1, 1],
                [1, 1, 0],
                [0, 1, 1],
            ]
        )
        == 4
    )
