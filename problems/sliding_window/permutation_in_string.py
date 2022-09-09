"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
    1 <= s1.length, s2.length <= 104
    s1 and s2 consist of lowercase English letters.
"""

from string import ascii_lowercase


def to_map(s):
    out = [0] * len(ascii_lowercase)
    for x in s:
        out[ord(x) - 97] += 1
    return out


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l = 0
        s1mem = to_map(s1)
        rstart = l + len(s1) - 1
        s2mem = to_map(s2[l : rstart + 1])
        matches = 0
        for i in range(len(ascii_lowercase)):
            if s1mem[i] == s2mem[i]:
                matches += 1

        for r in range(rstart + 1, len(s2)):
            if matches == len(ascii_lowercase):
                return True

            cr = s2[r]
            nr = ord(cr) - 97
            s2mem[nr] += 1
            if s2mem[nr] == s1mem[nr]:
                matches += 1
            elif s2mem[nr] == s1mem[nr] + 1:
                matches -= 1

            cl = s2[l]
            nl = ord(cl) - 97
            s2mem[nl] -= 1
            if s2mem[nl] == s1mem[nl]:
                matches += 1
            elif s2mem[nl] == s1mem[nl] - 1:
                matches -= 1
            l += 1

        return matches == len(ascii_lowercase)


if __name__ == "__main__":
    s = Solution()
    assert s.checkInclusion("ab", "eidbaooo") == True
    assert s.checkInclusion("abc", "eidbcaooo") == True
    assert s.checkInclusion("abc", "bbbca") == True
    assert s.checkInclusion("ab", "eidboaoo") == False
    assert s.checkInclusion("a", "ab") == True
