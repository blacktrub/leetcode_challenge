"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.)
(0,8),(8,10) is not conflict at 8

Example1
Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)

Example2
Input: intervals = [(2,7)]
Output: 1
Explanation: 
Only need one meeting room
"""

from typing import (
    List,
)


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        start = sorted([x.start for x in intervals])
        end = sorted([x.end for x in intervals])
        res, cnt = 0, 0
        sp, ep = 0, 0
        while sp < len(intervals):
            if start[sp] < end[ep]:
                sp += 1
                cnt += 1
            else:
                ep += 1
                cnt -= 1
            res = max(res, cnt)
        return res


# My solution
# class Solution:
#     """
#     @param intervals: an array of meeting time intervals
#     @return: the minimum number of conference rooms required
#     """
#
#     def min_meeting_rooms(self, intervals: List[Interval]) -> int:
#         intervals.sort(key=lambda x: x.start)
#         res = [intervals[0].end]
#         for p in intervals[1:]:
#             for i in range(len(res)):
#                 if p.start >= res[i]:
#                     res[i] = p.end
#                     break
#             else:
#                 res.append(p.end)
#         return len(res)


if __name__ == "__main__":
    assert (
        Solution().min_meeting_rooms(
            [
                Interval(0, 30),
                Interval(5, 10),
                Interval(15, 20),
            ]
        )
        == 2
    )
    # assert Solution().min_meeting_rooms([Interval(2, 7)]) == 1
    # assert Solution().min_meeting_rooms([Interval(2, 3), Interval(3, 6)]) == 1
