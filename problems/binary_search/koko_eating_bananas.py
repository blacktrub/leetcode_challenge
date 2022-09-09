"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23

Constraints:
    1 <= piles.length <= 104
    piles.length <= h <= 109
    1 <= piles[i] <= 109
"""


from typing import List
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        l, r = 1, max_pile
        m, k = 0, 0
        while l <= r:
            m = (l + r) // 2
            result = 0
            for x in piles:
                result += ceil(x / m)

            if result <= h:
                k = m
                r = m - 1
            else:
                l = m + 1
        return k


if __name__ == "__main__":
    s = Solution()
    assert s.minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert s.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert s.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
    assert s.minEatingSpeed([312884470], 312884469) == 2
