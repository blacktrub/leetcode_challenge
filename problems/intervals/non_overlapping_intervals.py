"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Constraints:
    1 <= intervals.length <= 105
    intervals[i].length == 2
    -5 * 104 <= starti < endi <= 5 * 104

TODO: there is a better solution
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        res = 1
        end = intervals[0][1]
        for s, e in intervals[1:]:
            if end <= s:
                res += 1
                end = e

        return len(intervals) - res


if __name__ == "__main__":
    assert Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert Solution().eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert Solution().eraseOverlapIntervals([[1, 100], [11, 22], [1, 11], [2, 12]]) == 2
    assert Solution().eraseOverlapIntervals([[1, 2], [1, 3], [1, 4]]) == 2
    assert (
        Solution().eraseOverlapIntervals(
            [
                [-52, 31],
                [-73, -26],
                [82, 97],
                [-65, -11],
                [-62, -49],
                [95, 99],
                [58, 95],
                [-31, 49],
                [66, 98],
                [-63, 2],
                [30, 47],
                [-40, -26],
            ]
        )
        == 7
    )
