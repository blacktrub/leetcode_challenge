"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]

Constraints:
    0 <= rowIndex <= 33

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
"""

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        prev = row
        for x in range(1, rowIndex + 2):
            row = [1] * x
            for y in range(x - 2):
                row[y + 1] = prev[y] + prev[y + 1]
            prev = row
        return row


if __name__ == "__main__":
    assert Solution().getRow(3) == [1, 3, 3, 1]
    assert Solution().getRow(0) == [1]
    assert Solution().getRow(1) == [1, 1]
