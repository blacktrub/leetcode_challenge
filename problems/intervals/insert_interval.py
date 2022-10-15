"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:
    0 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 105
    intervals is sorted by starti in ascending order.
    newInterval.length == 2
    0 <= start <= end <= 105
"""

from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        if intervals[0][0] > newInterval[1]:
            return [newInterval] + intervals

        if intervals[-1][1] < newInterval[0]:
            return intervals + [newInterval]

        res = []
        new_start, new_end = newInterval

        i = 0
        while i < len(intervals):
            s, e = intervals[i]
            if e < new_start:
                res.append([s, e])
            elif s > new_end:
                break
            else:
                new_start = min(s, new_start)
                new_end = max(e, new_end)

            i += 1

        return res + [[new_start, new_end]] + intervals[i:]


if __name__ == "__main__":
    assert Solution().insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert Solution().insert([[1, 3], [4, 9]], [2, 5]) == [[1, 9]]
    assert Solution().insert([[1, 5]], [0, 0]) == [[0, 0], [1, 5]]
    assert Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [
        [1, 2],
        [3, 10],
        [12, 16],
    ]
    assert Solution().insert([[1, 5]], [0, 5]) == [[0, 5]]
    assert Solution().insert([[2, 4], [5, 7], [8, 10], [11, 13]], [3, 6]) == [
        [2, 7],
        [8, 10],
        [11, 13],
    ]
