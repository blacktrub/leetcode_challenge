"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
    1 <= j <= nums[i] and
    i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2

Constraints:
    1 <= nums.length <= 104
    0 <= nums[i] <= 1000
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        left, right = 0, 1
        while right < len(nums):
            step = max(x + nums[x] for x in range(left, right))
            left = right
            right = step + 1
            res += 1

        return res


if __name__ == "__main__":
    assert Solution().jump([2, 3, 1, 1, 4]) == 2
    assert Solution().jump([2, 3, 0, 1, 4]) == 2
    assert Solution().jump([1, 2, 1, 1, 1]) == 3
    assert Solution().jump([3, 4, 3, 2, 5, 4, 3]) == 3
