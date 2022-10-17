"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.
A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:
    m == s.length
    n == t.length
    1 <= m, n <= 105
    s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = {}
        for x in t:
            cnt[x] = cnt.get(x, 0) + 1

        res = ""
        window = {}
        have, need = 0, len(cnt)
        l, r = 0, 0
        s = " " + s
        while True:

            if have < need:
                if r >= len(s) - 1:
                    break

                r += 1

                ch = s[r]
                if ch in cnt:
                    window[ch] = window.get(ch, 0) + 1
                    if window[ch] == cnt[ch]:
                        have += 1
            else:
                if not res:
                    res = s[l : r + 1]

                if len(res) > (r - l + 1):
                    res = s[l : r + 1]

                ch = s[l]
                if ch in cnt:
                    window[ch] = window[ch] - 1
                    if window[ch] < cnt[ch]:
                        have -= 1
                l += 1

                if r == len(s) - 1 and have < need:
                    break

        return res


if __name__ == "__main__":
    assert Solution().minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert Solution().minWindow("a", "a") == "a"
    assert Solution().minWindow("acbbaca", "aba") == "baca"
    assert Solution().minWindow("ab", "a") == "a"
    assert Solution().minWindow("abc", "ab") == "ab"
    assert Solution().minWindow("abc", "a") == "a"
    assert Solution().minWindow("bdab", "ab") == "ab"
    assert Solution().minWindow("aaflslflsldkalskaaa", "aaa") == "aaa"
    assert Solution().minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd") == "abbbbbcdd"
    assert Solution().minWindow("abcabdebac", "cda") == "cabd"
    assert Solution().minWindow("a", "aa") == ""
