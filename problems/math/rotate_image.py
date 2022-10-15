"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:
    n == matrix.length == matrix[i].length
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        (0,0), (0,2), (2,2), (2,0)
        """

        n = len(matrix)
        for i in range(n // 2):
            k = n - i - 1
            for j in range(i, n - i - 1):
                a = (i, j)
                b = (j, k)
                c = (k, n - 1 - j)
                d = (n - 1 - j, i)
                (
                    matrix[a[0]][a[1]],
                    matrix[b[0]][b[1]],
                    matrix[c[0]][c[1]],
                    matrix[d[0]][d[1]],
                ) = (
                    matrix[d[0]][d[1]],
                    matrix[a[0]][a[1]],
                    matrix[b[0]][b[1]],
                    matrix[c[0]][c[1]],
                )


if __name__ == "__main__":
    assert Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]
    assert Solution().rotate(
        [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    ) == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
