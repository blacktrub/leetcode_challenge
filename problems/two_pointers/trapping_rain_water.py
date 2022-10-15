"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
    n == height.length
    1 <= n <= 2 * 104
    0 <= height[i] <= 105
"""


from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        for i in range(1, max(height) + 1):
            j = 0
            while j < len(height):
                if height[j] < i:
                    j += 1
                    continue

                k = j + 1
                while k < len(height) and height[k] < i:
                    k += 1

                if k < len(height) and height[k] >= i:
                    res += k - j - 1

                j = k

        return res


if __name__ == "__main__":
    assert Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert Solution().trap([4, 2, 0, 3, 2, 5]) == 9
    assert Solution().trap([4, 2, 3]) == 1
