"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
An interleaving of two strings s and t is a configuration where s and t are divided into n and m non-empty substrings respectively, such that:
    s = s1 + s2 + ... + sn
    t = t1 + t2 + ... + tm
    |n - m| <= 1
    The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.

Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true

Constraints:
    0 <= s1.length, s2.length <= 100
    0 <= s3.length <= 200
    s1, s2, and s3 consist of lowercase English letters.

Follow up: Could you solve it using only O(s2.length) additional memory space?

TODO: there is a better DP solution https://neetcode.io/practice
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}

        def cut(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            k = i + j
            if i >= len(s1) and j >= len(s2) and k >= len(s3):
                return True

            if k >= len(s3):
                return False

            if i < len(s1) and s3[k] == s1[i] and cut(i + 1, j):
                dp[(i, j)] = True
                return True

            if j < len(s2) and s3[k] == s2[j] and cut(i, j + 1):
                dp[(i, j)] = True
                return True

            dp[(i, j)] = False
            return False

        return cut(0, 0)


if __name__ == "__main__":
    assert Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac") == True
    assert Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc") == False
    assert Solution().isInterleave("", "", "a") == False
    assert Solution().isInterleave("aabc", "abad", "aabcabad") == True
    assert Solution().isInterleave("aabcc", "dbbca", "aadbcbbcac") == True
