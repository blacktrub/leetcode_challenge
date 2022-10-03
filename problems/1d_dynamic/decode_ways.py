"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
    "AAJF" with the grouping (1 1 10 6)
    "KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
Given a string s containing only digits, return the number of ways to decode it.
The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").

Constraints:
    1 <= s.length <= 100
    s contains only digits and may contain leading zero(s).
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        if s.startswith("0"):
            return 0

        if len(s) < 2:
            return 1

        def is_valid(n):
            return 0 < int(n) < 27

        res = [1, 1]
        for x in range(2, len(s) + 1):
            if s[x - 1] == "0":
                if is_valid(s[x - 2 : x]):
                    res.append(res[x - 2])
                    continue
                else:
                    return 0

            if is_valid(s[x - 2 : x]) and s[x - 2] != "0":
                res.append(res[x - 2] + res[x - 1])
            else:
                res.append(res[x - 1])

        return res[-1]


if __name__ == "__main__":
    assert Solution().numDecodings("12") == 2
    assert Solution().numDecodings("226") == 3
    assert Solution().numDecodings("141") == 2
    assert Solution().numDecodings("10") == 1
    assert Solution().numDecodings("230") == 0
