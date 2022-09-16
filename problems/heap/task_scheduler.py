"""
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
Return the least number of units of times that the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

Example 3:
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

Constraints:
    1 <= task.length <= 104
    tasks[i] is upper-case English letter.
    The integer n is in the range [0, 100].
"""

from collections import deque
from typing import List
from heapq import heappop, heappush


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = {}
        for l in tasks:
            cnt[l] = cnt.get(l, 0) + 1

        heap = []
        for l, cnt in cnt.items():
            heappush(heap, (-cnt, l))

        t = 0
        q = deque()
        while heap or q:
            if q and q[0][0] == t:
                _, count, letter = q.popleft()
                heappush(heap, (count, letter))
            elif not heap:
                t += 1
                continue

            if heap:
                count, letter = heappop(heap)
                count += 1
                if count < 0:
                    q.append((t + n + 1, count, letter))

            t += 1

        return t


if __name__ == "__main__":
    s = Solution()
    assert s.leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8
