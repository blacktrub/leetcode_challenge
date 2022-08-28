"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        c1, c2 = {}, {}
        for i in range(len(s)):
            a, b = s[i], t[i]
            c1[a] = c1.get(a, 0) + 1
            c2[b] = c2.get(b, 0) + 1

        return c1 == c2


if __name__ == "__main__":
    s = Solution()
    assert s.isAnagram("anagram", "nagaram") == True
