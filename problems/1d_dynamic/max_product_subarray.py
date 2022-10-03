"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
A subarray is a contiguous subsequence of the array.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
    1 <= nums.length <= 2 * 104
    -10 <= nums[i] <= 10
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        p, np = 1, None
        for i in range(len(nums)):
            if nums[i] == 0:
                res = max(res, 0)
                p, np = 1, None
                continue

            s = p * nums[i]
            if s > 0:
                res = max(res, s)
            else:
                res = max(res, s // (np if np is not None else p))

            p = s
            np = p if p < 0 and not np else np

        return res


if __name__ == "__main__":
    assert Solution().maxProduct([2, 3, -2, 4]) == 6
    assert Solution().maxProduct([-2, 0, -1]) == 0
    assert Solution().maxProduct([0, 2]) == 2
    assert Solution().maxProduct([-2]) == -2
    assert Solution().maxProduct([-1, -2, -3, 0]) == 6
    assert Solution().maxProduct([2, -5, -2, -4, 3]) == 24
