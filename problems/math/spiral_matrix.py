"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        from enum import Enum

        class Motion(Enum):
            right = 0
            left = 1
            down = 2
            top = 3

        seen = set()

        sides = {
            Motion.right: Motion.down,
            Motion.down: Motion.left,
            Motion.left: Motion.top,
            Motion.top: Motion.right,
        }

        def spiral(i, j, m):
            if (
                i >= len(matrix)
                or j >= len(matrix[0])
                or i < 0
                or j < 0
                or (i, j) in seen
            ):
                return []

            if m == Motion.right and (j + 1 == len(matrix[0]) or (i, j + 1) in seen):
                m = sides[m]
            elif m == Motion.left and (j - 1 < 0 or (i, j - 1) in seen):
                m = sides[m]
            elif m == Motion.down and (i + 1 == len(matrix) or (i + 1, j) in seen):
                m = sides[m]
            elif m == Motion.top and (i - 1 < 0 or (i - 1, j) in seen):
                m = sides[m]

            elem = [matrix[i][j]]
            seen.add((i, j))
            match m:
                case Motion.right:
                    j += 1
                case Motion.left:
                    j -= 1
                case Motion.down:
                    i += 1
                case Motion.top:
                    i -= 1

            return elem + spiral(i, j, m)

        return spiral(0, 0, Motion.right)


if __name__ == "__main__":
    assert Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        1,
        2,
        3,
        6,
        9,
        8,
        7,
        4,
        5,
    ]
    assert Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [
        1,
        2,
        3,
        4,
        8,
        12,
        11,
        10,
        9,
        5,
        6,
        7,
    ]
    assert Solution().spiralOrder([[1]]) == [1]
    assert Solution().spiralOrder([[2], [3]]) == [2, 3]
    assert Solution().spiralOrder([[2, 3], [5, 4]]) == [2, 3, 4, 5]
