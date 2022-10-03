"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:
    1 <= nums.length <= 2500
    -104 <= nums[i] <= 104

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

TODO: there is a better solution
https://www.youtube.com/watch?v=S9oUiVYEq7E
https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326308/C%2B%2BPython-DP-Binary-Search-BIT-Solutions-Picture-explain-O(NlogN)
"""


from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [1] * len(nums)
        m = 1
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    res[i] = max(res[i], res[j] + 1)
            m = max(m, res[i])
        return m


# DFS with cache
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         res = [0] * len(nums)
#
#         def dfs(i):
#             if i >= len(nums):
#                 return 0
#
#             if res[i]:
#                 return res[i]
#
#             m = 0
#             for x in range(i, len(nums)):
#                 if nums[x] > nums[i]:
#                     m = max(m, dfs(x))
#             res[i] = m + 1
#             return m + 1
#
#         m = 0
#         for i in range(len(nums) - 1, -1, -1):
#             m = max(m, dfs(i))
#
#         return m


if __name__ == "__main__":
    assert Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
    assert Solution().lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1
    assert Solution().lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6
