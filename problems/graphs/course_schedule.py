"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:
    1 <= numCourses <= 2000
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    All the pairs prerequisites[i] are unique.
"""

from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        req = defaultdict(set)
        for course, prereq in prerequisites:
            req[course].add(prereq)

        def dfs(i, seen):
            if i >= numCourses or i not in req or not req[i]:
                return True

            if i in seen:
                return False

            seen.add(i)
            for r in req[i].copy():
                if dfs(r, seen):
                    req[i].remove(r)
                else:
                    return False
            return True

        res = True
        for x in range(numCourses):
            res = res and dfs(x, set())
        return res


if __name__ == "__main__":
    s = Solution()
    assert (
        s.canFinish(
            8,
            [
                [1, 0],
                [2, 6],
                [1, 7],
                [6, 4],
                [7, 0],
                [0, 5],
            ],
        )
        == True
    )
    assert s.canFinish(2, [[1, 0], [0, 1]]) == False
    assert (
        s.canFinish(
            20,
            [
                [0, 10],
                [3, 18],
                [5, 5],
                [6, 11],
                [11, 14],
                [13, 1],
                [15, 1],
                [17, 4],
            ],
        )
        == False
    )
