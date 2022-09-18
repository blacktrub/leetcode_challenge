"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def make_pairs(arr):
            if len(arr) == 1:
                return [arr]

            if len(arr) == 2:
                return [[arr[0], arr[1]], [arr[1], arr[0]]]

            res = []
            for x in range(len(arr)):
                tmp = arr.copy()
                elem = tmp[x]
                tmp[0], tmp[x] = tmp[x], tmp[0]
                pairs = make_pairs(tmp[1:])
                for y in range(len(pairs)):
                    pairs[y].append(elem)
                    res.append(pairs[y])
            return res

        res = make_pairs(nums)
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.permute([0, 1]) == [[0, 1], [1, 0]]
    assert s.permute([1]) == [[1]]
    assert sorted(s.permute([1, 2, 3])) == sorted(
        [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
        ]
    )
