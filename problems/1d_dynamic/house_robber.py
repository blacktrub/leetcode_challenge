"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 400
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # f(0) = 0
        # f(1) = a0
        # f(2) = max(f(1), a1 + f(0))
        # f(3) = max(f(2), a2 + f(1))
        # f(4) = max(f(3), a3 + f(2))
        # f(x) = max(f(x-1), ax-1 + f(x-2))
        if len(nums) < 2:
            return nums[0]

        sm = [0, nums[0]]
        for i in range(2, len(nums) + 1):
            sm.append(max(sm[i - 1], nums[i - 1] + sm[i - 2]))
        return sm[-1]


if __name__ == "__main__":
    assert Solution().rob([1, 2, 3, 1]) == 4
    assert Solution().rob([2, 7, 9, 3, 1]) == 12
    assert Solution().rob([0]) == 0
    assert Solution().rob([2, 1, 1, 2]) == 4
