"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]

Constraints:
    1 <= numCourses <= 2000
    0 <= prerequisites.length <= numCourses * (numCourses - 1)
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    ai != bi
    All the pairs [ai, bi] are distinct.
"""

from typing import List
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return list(range(numCourses))

        req = defaultdict(set)
        for x, y in prerequisites:
            req[x].add(y)

        has_order = set()
        seen = set()

        def dfs(i):
            if i in has_order:
                return [], True

            if i >= numCourses or i not in req or not req[i]:
                has_order.add(i)
                return [i], True

            has_order.add(i)
            seen.add(i)
            path = []
            for c in req[i].copy():
                if c in seen:
                    return [], False

                p, result = dfs(c)
                if not result:
                    return [], False
                path += p
            seen.remove(i)
            return path + [i], True

        res = []
        for x in range(numCourses):
            if x in req:
                path, result = dfs(x)
                if not result:
                    return []

                res += path
            elif x not in has_order:
                res.append(x)
                has_order.add(x)

        return res


if __name__ == "__main__":
    s = Solution()
    assert s.findOrder(2, [[1, 0]]) == [0, 1]
    assert s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 1, 2, 3]
    assert s.findOrder(1, []) == [0]
    assert s.findOrder(2, [[0, 1], [1, 0]]) == []
    assert s.findOrder(3, [[1, 0]]) == [0, 1, 2]
    assert (
        s.findOrder(
            7,
            [
                [1, 0],
                [0, 3],
                [0, 2],
                [3, 2],
                [2, 5],
                [4, 5],
                [5, 6],
                [2, 4],
            ],
        )
        == [6, 5, 4, 2, 3, 0, 1]
    )
