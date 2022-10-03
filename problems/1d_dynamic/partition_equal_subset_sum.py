"""
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

Constraints:
    1 <= nums.length <= 200
    1 <= nums[i] <= 100
"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sm = sum(nums)
        if total_sm % 2 != 0:
            return False

        total = total_sm // 2
        res = {0}

        for i in range(len(nums) - 1, -1, -1):
            for x in res.copy():
                sm = x + nums[i]
                if sm == total and total in res:
                    return True
                res.add(sm)
        return False


if __name__ == "__main__":
    assert Solution().canPartition([1, 5, 11, 5]) == True
    assert Solution().canPartition([1, 2, 3, 5]) == False
