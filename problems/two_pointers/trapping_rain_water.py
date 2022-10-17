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
        max_left, max_right = 0, 0
        res = 0
        i, j = 0, len(height) - 1
        while i != j:
            if height[i] < height[j]:
                if (max_left - height[i]) > 0:
                    res += max_left - height[i]

                max_left = max(max_left, height[i])
                i += 1
            else:
                if (max_right - height[j]) > 0:
                    res += max_right - height[j]

                max_right = max(max_right, height[j])
                j -= 1

        return res


if __name__ == "__main__":
    assert Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert Solution().trap([4, 2, 0, 3, 2, 5]) == 9
    assert Solution().trap([4, 2, 3]) == 1
