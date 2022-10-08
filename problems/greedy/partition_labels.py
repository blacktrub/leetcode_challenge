"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
Return a list of integers representing the size of these parts.

Example 1:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Example 2:
Input: s = "eccbbbbdec"
Output: [10]

Constraints:
    1 <= s.length <= 500
    s consists of lowercase English letters.
"""

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_to_idx = {}
        for i in range(len(s)):
            char_to_idx[s[i]] = i

        i, goal, curr_len = 0, 0, 0
        res = []
        while i < len(s):
            ch = s[i]
            goal = max(goal, char_to_idx[ch])
            curr_len += 1

            if i == goal:
                res.append(curr_len)
                curr_len = 0

            i += 1

        return res


if __name__ == "__main__":
    assert Solution().partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
    assert Solution().partitionLabels("qiejxqfnqceocmy") == [13, 1, 1]
