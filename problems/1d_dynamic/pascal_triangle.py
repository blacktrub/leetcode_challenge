"""
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]

Constraints:
    1 <= numRows <= 30
"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        res = [[1], [1, 1]]
        for x in range(3, numRows + 1):
            row = [1] * x
            for y in range(x - 2):
                row[y + 1] = res[x - 2][y] + res[x - 2][y + 1]
            res.append(row)
        return res


if __name__ == "__main__":
    assert Solution().generate(5) == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
    ]
    assert Solution().generate(1) == [[1]]
