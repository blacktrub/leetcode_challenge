"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:
    1 <= nums.length <= 105
    nums[i] is either 0 or 1.
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        c, r = 0, 0
        for x in nums:
            if x:
                c += 1
                r = max(c, r)
            else:
                c = 0
        return r


if __name__ == "__main__":
    s = Solution()
    assert s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3
    assert s.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) == 2
