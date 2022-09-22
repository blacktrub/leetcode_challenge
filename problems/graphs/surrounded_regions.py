"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.

Example 2:
Input: board = [["X"]]
Output: [["X"]]

Constraints:
    m == board.length
    n == board[i].length
    1 <= m, n <= 200
    board[i][j] is 'X' or 'O'.
"""

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def dfs(row, col):
            if (
                row < 0
                or col < 0
                or row >= rows
                or col >= cols
                or board[row][col] != "O"
            ):
                return

            board[row][col] = "C"
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for x in range(rows):
            for y in range(cols):
                if board[x][y] == "O" and (x in (0, rows - 1) or y in (0, cols - 1)):
                    dfs(x, y)

        for x in range(rows):
            for y in range(cols):
                if board[x][y] == "O":
                    board[x][y] = "X"

        for x in range(rows):
            for y in range(cols):
                if board[x][y] == "C":
                    board[x][y] = "O"


if __name__ == "__main__":
    s = Solution()
    board = [
        ["O", "X", "X", "O", "X"],
        ["X", "O", "O", "X", "O"],
        ["X", "O", "X", "O", "X"],
        ["O", "X", "O", "O", "O"],
        ["X", "X", "O", "X", "O"],
    ]
    s.solve(board)
    assert board == [
        ["O", "X", "X", "O", "X"],
        ["X", "X", "X", "X", "O"],
        ["X", "X", "X", "O", "X"],
        ["O", "X", "O", "O", "O"],
        ["X", "X", "O", "X", "O"],
    ], board


[
    ["X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "O", "X"],
    ["X", "X", "X", "O", "O", "X"],
]


[
    ["O", "O", "O", "O", "X", "X"],
    ["O", "O", "O", "O", "O", "O"],
    ["O", "X", "O", "X", "O", "O"],
    ["O", "X", "O", "O", "X", "O"],
    ["O", "X", "O", "X", "O", "O"],
    ["O", "X", "O", "O", "O", "O"],
]
