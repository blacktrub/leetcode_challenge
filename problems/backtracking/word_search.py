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
        def find_steps(first, second):
            m, n = len(board), len(board[0])
            steps = []
            if second - 1 >= 0:
                steps.append((first, second - 1))
            if second + 1 < n:
                steps.append((first, second + 1))
            if first - 1 >= 0:
                steps.append((first - 1, second))
            if first + 1 < m:
                steps.append((first + 1, second))
            return steps

        def next_board_step(j):
            n = len(board[0])
            j = (j[0], j[1] + 1)
            if j[1] >= n:
                j = (j[0] + 1, 0)
            return j

        def find_match(i, left, right, path):
            m, n = len(board), len(board[0])
            if i >= len(word):
                return True

            if left >= m:
                return False

            if left > m and right > n:
                return False

            if i == len(word) - 1 and word[i] == board[left][right]:
                return True

            if word[i] == board[left][right]:
                new_path = path.copy()
                new_path.add((left, right))
                steps = find_steps(left, right)

                for x, y in steps:
                    if (x, y) in new_path:
                        continue

                    if word[i + 1] == board[x][y]:
                        result = find_match(i + 1, x, y, new_path)
                        if result:
                            return True

            if path:
                return False

            return find_match(0, *next_board_step((left, right)), set())

        return find_match(0, 0, 0, set())


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
