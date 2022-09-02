"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2: Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

Constraints:
    2 <= cost.length <= 1000
    0 <= cost[i] <= 999
"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_per_x = [0] * len(cost)
        cost_per_x[0] = cost[0]
        cost_per_x[1] = cost[1]
        for i in range(2, len(cost)):
            n1 = cost_per_x[i - 1]
            n2 = cost_per_x[i - 2]
            cost_per_x[i] = min(n1, n2) + cost[i]
        return min(cost_per_x[-1], cost_per_x[-2])


if __name__ == "__main__":
    s = Solution()
    assert s.minCostClimbingStairs([10, 15, 20]) == 15
    assert s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
