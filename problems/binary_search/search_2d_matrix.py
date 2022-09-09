"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -104 <= matrix[i][j], target <= 104
"""


from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        lm, rm, matrix_mid = 0, m - 1, 0
        while lm <= rm:
            matrix_mid = (lm + rm) // 2
            if matrix[matrix_mid][0] > target:
                rm = matrix_mid - 1
            else:
                lm = matrix_mid + 1

        matrix_mid = (lm + rm) // 2

        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[matrix_mid][mid] == target:
                return True
            elif matrix[matrix_mid][mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False


if __name__ == "__main__":
    s = Solution()
    assert s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) == True
    assert (
        s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) == False
    )
    assert s.searchMatrix([[1], [3]], 1) == True
    print("ok")
