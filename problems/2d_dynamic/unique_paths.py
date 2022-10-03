"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Constraints:
    1 <= m, n <= 100
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = []
        for _ in range(m):
            grid.append([1] * n)

        for x in range(1, m):
            for y in range(1, n):
                grid[x][y] = grid[x - 1][y] + grid[x][y - 1]

        return grid[m - 1][n - 1]


if __name__ == "__main__":
    assert Solution().uniquePaths(3, 7) == 28
    assert Solution().uniquePaths(1, 1) == 1
    assert Solution().uniquePaths(5, 5) == 28
