"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
    1 <= s.length <= 300
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 20
    s and wordDict[i] consist of only lowercase English letters.
    All the strings of wordDict are unique.
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = [False] * (len(s) + 1)
        res[0] = True

        for i in range(len(s) + 1):
            for w in wordDict:
                if s[:i].endswith(w) and res[i - len(w)]:
                    res[i] = True
                    break

        return res[-1]


if __name__ == "__main__":
    assert Solution().wordBreak("leetcode", ["leet", "code"]) == True
    assert Solution().wordBreak("applepenapple", ["apple", "pen"]) == True
    assert (
        Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
        == False
    )
    assert Solution().wordBreak("aaaaaaa", ["aaaa", "aaa"]) == True
    assert (
        Solution().wordBreak(
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
            [
                "a",
                "aa",
                "aaa",
                "aaaa",
                "aaaaa",
                "aaaaaa",
                "aaaaaaa",
                "aaaaaaaa",
                "aaaaaaaaa",
                "aaaaaaaaaa",
            ],
        )
        == False
    )
