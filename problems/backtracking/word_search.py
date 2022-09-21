"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def find_match(i, left, right):
            if i == len(word):
                return True

            if (
                left < 0
                or right < 0
                or left >= rows
                or right >= cols
                or word[i] != board[left][right]
            ):
                return False

            org = board[left][right]
            board[left][right] = "-"
            res = (
                find_match(i + 1, left + 1, right)
                or find_match(i + 1, left - 1, right)
                or find_match(i + 1, left, right + 1)
                or find_match(i + 1, left, right - 1)
            )
            board[left][right] = org
            return res

        for x in range(rows):
            for y in range(cols):
                if find_match(0, x, y):
                    return True
        return False


if __name__ == "__main__":
    s = Solution()
    assert (
        s.exist(
            [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            "ABCCED",
        )
        == True
    )
    assert (
        s.exist(
            [
                ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "A"],
            ],
            "AAAAAAAAAAAAAAB",
        )
        == False
    )
