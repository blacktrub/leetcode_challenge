"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
You may assume that you have an infinite number of each kind of coin.
The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
Input: amount = 10, coins = [10]
Output: 1

Constraints:
    1 <= coins.length <= 300
    1 <= coins[i] <= 5000
    All the values of coins are unique.
    0 <= amount <= 5000
"""
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # DP
        dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)
        for a in range(1, amount + 1):
            for i in range(len(coins) - 1, -1, -1):
                dp[a][i] = dp[a][i + 1]
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]
        return dp[amount][0]

        # if not amount:
        #     return 1
        #
        # dp = {}
        #
        # def count_pairs(i, a):
        #     if (i, a) in dp:
        #         return dp[(i, a)]
        #     if i < 0 or i >= len(coins):
        #         return 0
        #
        #     if a - coins[i] < 0:
        #         return 0
        #
        #     if a - coins[i] == 0:
        #         return 1
        #
        #     pairs = 0
        #     for x in range(i, -1, -1):
        #         pairs += count_pairs(x, a - coins[i])
        #     dp[(i, a)] = pairs
        #     return pairs
        #
        # res = 0
        # for x in range(len(coins)):
        #     res += count_pairs(x, amount)
        # return res


if __name__ == "__main__":
    assert Solution().change(5, [1, 2, 5]) == 4
    assert Solution().change(3, [2]) == 0
    assert Solution().change(10, [10]) == 1
    # assert Solution().change(0, [7]) == 1
