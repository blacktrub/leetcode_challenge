"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
A palindrome string is a string that reads the same backward as forward.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]

Constraints:
    1 <= s.length <= 16
    s contains only lowercase English letters.
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        res, sub = [], []

        def dfs(i):
            if i >= len(s):
                res.append(sub.copy())
                return

            for j in range(i, len(s)):
                if is_palindrome(s[i : j + 1]):
                    sub.append(s[i : j + 1])
                    dfs(j + 1)
                    sub.pop()

        dfs(0)
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.partition("aab") == [["a", "a", "b"], ["aa", "b"]]
    assert s.partition("a") == [["a"]]
    assert s.partition("cdd") == [["c", "d", "d"], ["c", "dd"]]
