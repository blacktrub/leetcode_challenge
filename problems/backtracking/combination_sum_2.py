"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]

Constraints:
    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30
"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, sub = [], []

        def combinate(i, total):
            if total == target:
                res.append(sub.copy())
                return

            if i >= len(candidates):
                return

            if total > target:
                return

            elem = candidates[i]
            sub.append(candidates[i])
            combinate(i + 1, total + candidates[i])
            sub.pop()

            while i < len(candidates) and candidates[i] == elem:
                i += 1

            combinate(i, total)

        combinate(0, 0)
        return res


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)) == sorted(
        [
            [1, 1, 6],
            [1, 2, 5],
            [1, 7],
            [2, 6],
        ]
    )
    assert s.combinationSum2([1, 2, 1, 4], 4) == [
        [1, 1, 2],
        [4],
    ]
