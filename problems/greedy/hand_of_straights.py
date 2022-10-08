"""
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.
Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

Example 1:
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

Example 2:
Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.

Constraints:
    1 <= hand.length <= 104
    0 <= hand[i] <= 109
    1 <= groupSize <= hand.length

Note: This question is the same as 1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
"""

from collections import deque
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand = sorted(hand)

        q = deque()
        i = 0
        while i < len(hand):
            if q and i > 0 and hand[i] != hand[i - 1] + 1:
                return False

            c = 0
            j = i
            while j < len(hand) and hand[j] == hand[i]:
                c += 1
                j += 1

            if c < len(q):
                return False

            for _ in range(c - len(q)):
                q.append(hand[i])

            while q and groupSize - 1 == hand[i] - q[0]:
                q.popleft()

            i = j
        return len(q) == 0


if __name__ == "__main__":
    assert Solution().isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3) == True
    assert Solution().isNStraightHand([8, 10, 12], 3) == False
    assert Solution().isNStraightHand([1, 2, 3], 1) == True
    assert Solution().isNStraightHand([8, 8, 9, 7, 7, 7, 6, 7, 10, 6], 2) == True
