"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Constraints:
    1 <= n <= 105
    nums.length == n + 1
    1 <= nums[i] <= n
    All the integers in nums appear only once except for precisely one integer which appears two or more times.

Follow up:
    How can we prove that at least one duplicate number must exist in nums?
    Can you solve the problem in linear runtime complexity?
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return nums[0]

        fast, slow = 0, 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break

        second_slow = 0
        while second_slow != slow:
            slow = nums[slow]
            second_slow = nums[second_slow]

        return slow


if __name__ == "__main__":
    s = Solution()
    assert s.findDuplicate([1, 3, 4, 2, 2]) == 2
    assert s.findDuplicate([2, 2, 2, 2, 2]) == 2
    assert s.findDuplicate([1, 1]) == 1
    assert s.findDuplicate([1, 1, 2]) == 1
    assert s.findDuplicate([2, 5, 9, 6, 9, 3, 8, 9, 7, 1]) == 9
