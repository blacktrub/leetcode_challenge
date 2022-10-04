# TODO: I think there is a better solution

from typing import List
from heapq import heappush, heappop


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        dp = [0] * len(colors)

        i = 1
        while i < len(colors):
            dp[i] = dp[i - 1]
            if colors[i] == colors[i - 1]:
                t, c = i, 1
                heap = []
                heappush(heap, neededTime[t - 1])
                while t < len(colors) and colors[t] == colors[t - 1]:
                    heappush(heap, neededTime[t])
                    t += 1
                    c += 1

                total = dp[i]
                for _ in range(c - 1):
                    total += heappop(heap)

                for j in range(i, t):
                    dp[j] = total

                i = t
                continue

            i += 1

        return dp[-1]


if __name__ == "__main__":
    assert Solution().minCost("abaac", [1, 2, 3, 4, 5]) == 3
    assert Solution().minCost("abc", [1, 2, 3]) == 0
    assert Solution().minCost("aabaa", [1, 2, 3, 4, 1]) == 2
    assert Solution().minCost("aaabbbabbbb", [3, 5, 10, 7, 5, 3, 5, 5, 4, 8, 1]) == 26
