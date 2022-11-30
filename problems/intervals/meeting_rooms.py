"""
https://www.lintcode.com/problem/920/

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example1
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: 
(0,30), (5,10) and (0,30),(15,20) will conflict

Example2
Input: intervals = [(5,8),(9,15)]
Output: true
Explanation: 
Two times will not conflict 
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
    @return: if a person could attend all meetings
    """

    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda x: x.start)
        prev = intervals[0].end
        for p in intervals[1:]:
            if p.start < prev:
                return False
            prev = p.end
        return True


if __name__ == "__main__":
    assert (
        Solution().can_attend_meetings(
            [
                Interval(0, 30),
                Interval(5, 10),
                Interval(15, 20),
            ]
        )
        == False
    )
    assert (
        Solution().can_attend_meetings(
            [
                Interval(465, 497),
                Interval(386, 462),
                Interval(354, 380),
                Interval(134, 189),
                Interval(199, 282),
                Interval(18, 104),
                Interval(499, 562),
                Interval(4, 14),
                Interval(111, 129),
                Interval(292, 345),
            ]
        )
        == True
    )
