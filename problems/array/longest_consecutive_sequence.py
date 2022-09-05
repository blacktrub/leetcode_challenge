"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
"""


from typing import List


# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         nums = sorted(list(set(nums)))
#         c, out = 1, 0
#         for i in range(1, len(nums)):
#             if (nums[i] - nums[i - 1]) == 1:
#                 c += 1
#             else:
#                 out = max(out, c)
#                 c = 1
#         out = max(out, c)
#         return out


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        mem = set(nums)
        long = 0
        for x in nums:
            if x - 1 in mem:
                continue

            count = 0
            while count + x in mem:
                count += 1
            long = max(long, count)

        return long


if __name__ == "__main__":
    s = Solution()
    assert s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
