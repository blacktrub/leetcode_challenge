"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
    3 <= nums.length <= 3000
    -105 <= nums[i] <= 105
"""


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        out = []

        for x in range(len(nums)):
            if x > 0 and nums[x] == nums[x - 1]:
                continue

            left, right = x + 1, len(nums) - 1
            while left < right:
                s = nums[x] + nums[left] + nums[right]
                if s == 0:
                    out.append([nums[x], nums[left], nums[right]])
                    left += 1
                    while nums[left - 1] == nums[left] and left < right:
                        left += 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1

        return out


if __name__ == "__main__":
    s = Solution()
    assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
