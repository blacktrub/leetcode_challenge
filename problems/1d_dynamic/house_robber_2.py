"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 1000
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # f(1) = nums[x-1=0]
        # f(x) = max(f(x-1), f(x-2)+Ax-1)
        if len(nums) < 2:
            return nums[0]

        res = [0, nums[0]]
        for x in range(2, len(nums)):
            res.append(max(res[x - 1], res[x - 2] + nums[x - 1]))

        res2 = [0, nums[1]]
        for x in range(2, len(nums)):
            res2.append(max(res2[x - 1], res2[x - 2] + nums[x]))
        return max(res[-1], res2[-1])


if __name__ == "__main__":
    assert Solution().rob([2, 3, 2]) == 3
    assert Solution().rob([1, 2, 3, 1]) == 4
    assert Solution().rob([1, 2, 3]) == 3
