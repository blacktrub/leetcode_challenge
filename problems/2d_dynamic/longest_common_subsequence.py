"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
    For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:
    1 <= text1.length, text2.length <= 1000
    text1 and text2 consist of only lowercase English characters.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text2) + 1, len(text1) + 1
        grid = []
        for _ in range(m):
            grid.append([0] * n)

        for i in range(1, m):
            for j in range(1, n):
                if text1[j - 1] == text2[i - 1]:
                    grid[i][j] = grid[i - 1][j - 1] + 1
                else:
                    grid[i][j] = max(grid[i][j - 1], grid[i - 1][j])

        return grid[m - 1][n - 1]


if __name__ == "__main__":
    assert Solution().longestCommonSubsequence("abcde", "ace") == 3
    assert Solution().longestCommonSubsequence("abc", "def") == 0
    assert Solution().longestCommonSubsequence("bl", "yby") == 1
    assert Solution().longestCommonSubsequence("oxcpqrsvwf", "shmtulqrypy") == 2
    assert Solution().longestCommonSubsequence("ezupkr", "ubmrapg") == 2
    assert Solution().longestCommonSubsequence("hofubmnylkra", "pqhgxgdofcvmr") == 5
    assert Solution().longestCommonSubsequence("bsbininm", "jmjkbkjkv") == 1
    assert Solution().longestCommonSubsequence("abcba", "abcbcba") == 5
