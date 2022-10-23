"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            if not prefix:
                return ""
            word = strs[i]
            while prefix and prefix != word[: len(prefix)]:
                prefix = prefix[: len(prefix) - 1]
        return prefix


if __name__ == "__main__":
    assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ""
