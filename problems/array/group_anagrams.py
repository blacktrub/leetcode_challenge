"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.

"""

from typing import List
from string import ascii_lowercase


def str_to_tuple(s):
    t = [0] * len(ascii_lowercase)
    for l in s:
        key = ord(l) - ord("a")
        t[key] += 1
    return tuple(t)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem = {}
        for x in strs:
            key = str_to_tuple("".join(sorted(x)))
            if key in mem:
                mem[key].append(x)
            else:
                mem[key] = [x]
        return list(mem.values())


if __name__ == "__main__":
    s = Solution()
    val = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert val == [
        ["bat"],
        ["nat", "tan"],
        ["ate", "eat", "tea"],
    ], val
