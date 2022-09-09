"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

Constraints:
    1 <= s.length <= 105
    s consists of only uppercase English letters.
    0 <= k <= s.length
"""

from string import ascii_uppercase


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, result = 0, 0
        mem = {}

        for r in range(len(s)):
            mem[s[r]] = mem.get(s[r], 0) + 1

            mx = 0
            for ch in ascii_uppercase:
                mx = max(mx, mem.get(ch, 0))

            longest = (r - l + 1) - mx

            while longest > k:
                mem[s[l]] = mem[s[l]] - 1
                l += 1
                longest = (r - l + 1) - mx

            result = max(result, r - l + 1)
            r += 1

        return result


if __name__ == "__main__":
    s = Solution()
    assert s.characterReplacement("ABAB", 2) == 4
    assert s.characterReplacement("AABABBA", 1) == 4
    assert s.characterReplacement("AAAB", 0) == 3
    assert s.characterReplacement("ABAA", 0) == 2
    assert s.characterReplacement("ABBB", 2) == 4
    assert s.characterReplacement("ABCDE", 2) == 3
    print("ok")
