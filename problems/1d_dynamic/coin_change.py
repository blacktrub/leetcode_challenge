"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Constraints:
    1 <= coins.length <= 12
    1 <= coins[i] <= 231 - 1
    0 <= amount <= 104
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {}

        def min_change(a):
            if a in mem:
                return mem[a]

            if a < 0:
                return -1

            if a == 0:
                return 0

            res = []
            for c in coins:
                r = min_change(a - c)
                if r != -1:
                    res.append(r)

            if res:
                m = min(res) + 1
            else:
                m = -1

            mem[a] = m
            return m

        return min_change(amount)


if __name__ == "__main__":
    assert Solution().coinChange([1, 2, 5], 11) == 3
    assert Solution().coinChange([2], 3) == -1
    assert Solution().coinChange([1], 0) == 0
    assert Solution().coinChange([1, 3, 4], 9) == 3
    assert Solution().coinChange([1, 6, 7], 12) == 2
    assert Solution().coinChange([1, 2, 5], 100) == 20
    assert Solution().coinChange([186, 419, 83, 408], 6249) == 20
