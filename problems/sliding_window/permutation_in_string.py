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


# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         if len(s1) > len(s2):
#             return False
#
#         if len(s1) == 1:
#             return s1 in s2
#
#         ch_to_idx = lambda ch: ord(ch) - ord("a")
#
#         cnt = [0] * 26
#         for ch in s1:
#             cnt[ch_to_idx(ch)] += 1
#
#         cur = [0] * 26
#         i, j = 0, len(s1)
#         for x in range(j):
#             cur[ch_to_idx(s2[x])] += 1
#
#         found = 0
#         for i in range(len(cnt)):
#             if cnt[i] == cur[i]:
#                 found += 1
#
#         i = 0
#         while j < len(s2):
#             if found == 26:
#                 return True
#
#             ch = s2[j]
#             idx = ch_to_idx(ch)
#             cur[idx] += 1
#
#             if cnt[idx] == cur[idx]:
#                 found += 1
#             elif cnt[idx] + 1 == cur[idx]:
#                 found -= 1
#
#             iidx = ch_to_idx(s2[i])
#             cur[iidx] -= 1
#             if cnt[iidx] == cur[iidx]:
#                 found += 1
#             elif cnt[iidx] - 1 == cur[iidx]:
#                 found -= 1
#
#             i += 1
#             j += 1
#
#         return found == 26


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        cnt = {}
        for ch in s1:
            cnt[ch] = cnt.get(ch, 0) + 1

        cur = {}
        i, j = 0, len(s1)
        for x in range(j):
            cur[s2[x]] = cur.get(s2[x], 0) + 1

        found = 0
        for key in cnt:
            if cnt[key] == cur.get(key, 0):
                found += 1

        while j < len(s2):
            if found == len(cnt):
                return True

            ch = s2[j]
            cur[ch] = cur.get(ch, 0) + 1

            if ch in cnt and cnt.get(ch, 0) == cur.get(ch, 0):
                found += 1
            elif ch in cnt and cnt.get(ch, 0) + 1 == cur.get(ch, 0):
                found -= 1

            if cur[ch] == 0:
                del cur[ch]

            ch = s2[i]
            cur[ch] = cur[ch] - 1
            if ch in cnt and cnt.get(ch, 0) == cur[ch]:
                found += 1
            elif ch in cnt and cnt.get(ch, 0) - 1 == cur[ch]:
                found -= 1

            if cur[ch] == 0:
                del cur[ch]

            i += 1
            j += 1

        return found == len(cnt)


if __name__ == "__main__":
    s = Solution()
    assert s.checkInclusion("adc", "dcda") == True
    assert s.checkInclusion("ab", "eidbaooo") == True
    assert s.checkInclusion("abc", "eidbcaooo") == True
    assert s.checkInclusion("abc", "bbbca") == True
    assert s.checkInclusion("ab", "eidboaoo") == False
    assert s.checkInclusion("a", "ab") == True
    assert s.checkInclusion("12", "321") == True
    assert s.checkInclusion(".,", "asdasd,.asd") == True
