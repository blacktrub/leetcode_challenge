"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
"""

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        counts = {}
        for x in nums:
            counts[x] = counts.get(x, 0) + 1

        res = [[]]
        for key, count in counts.items():
            cases = []
            for x in range(1, count + 1):
                for r in res:
                    cases.append(r + [key] * x)
            res += cases

        return res


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.subsetsWithDup([1, 2, 2])) == sorted(
        [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    )
