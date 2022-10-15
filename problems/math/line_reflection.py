"""
Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.

Example1
Input: [[1,1],[-1,1]]
Output: true

Example2
Input: [[1,1],[-1,-1]]
Output: false

Challenge
Could you do better than O(n2)?
"""

from typing import List


class Solution:
    """
    @param points: n points on a 2D plane
    @return: if there is such a line parallel to y-axis that reflect the given points
    """

    def is_reflected(self, points: List[List[int]]) -> bool:
        points.sort()
        m = len(points) // 2
        i, j = m - 1, m
        if len(points) % 2 == 0:
            line = None
        else:
            line = points[m][0]

        while i >= 0 and j < len(points):
            lp, rp = points[i], points[j]
            if lp[1] != rp[1]:
                return False

            if line:
                new_line = ((rp[0] - lp[0]) // 2) + lp[0]
                if line != new_line:
                    return False

            line = ((rp[0] - lp[0]) // 2) + lp[0]

            i -= 1
            j += 1

        return True


if __name__ == "__main__":
    assert Solution().is_reflected([[1, 1], [-1, 1]]) == True
    assert Solution().is_reflected([[1, 1], [-1, -1]]) == False
    assert Solution().is_reflected([[2, 2], [-2, 2], [1, 1], [-1, 1]]) == True
    assert Solution().is_reflected([[0, 0], [1, 0], [3, 0]]) == False
