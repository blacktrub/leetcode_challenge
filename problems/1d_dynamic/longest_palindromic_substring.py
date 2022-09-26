"""
Given a string s, return the longest palindromic substring in s.
A string is called a palindrome string if the reverse of that string is the same as the original string.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
    1 <= s.length <= 1000
    s consist of only digits and English letters.
"""

from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        if is_palindrome(s):
            return s

        m = ""
        for i in range(len(s)):
            cur = s[i]
            l, r = i, i
            if i > 0 and s[i] == s[i - 1]:
                cur += s[i - 1]
                l -= 1

            if i < len(s) - 1 and s[i] == s[i + 1]:
                cur += s[i + 1]
                r += 1

            if l > 0 and r < len(s) - 1 and s[l - 1] == s[r + 1]:
                while l > 0 and r < len(s) - 1 and s[l] == s[r]:
                    if s[l - 1] == s[r + 1]:
                        l -= 1
                        r += 1
                    else:
                        break

                cur = s[l : r + 1]
            if len(cur) > len(m):
                m = cur
        return m


if __name__ == "__main__":
    # assert Solution().longestPalindrome("caba") == "aba"
    assert (
        Solution().longestPalindrome(
            "azwdzwmwcqzgcobeeiphemqbjtxzwkhiqpbrprocbppbxrnsxnwgikiaqutwpftbiinlnpyqstkiqzbggcsdzzjbrkfmhgtnbujzszxsycmvipjtktpebaafycngqasbbhxaeawwmkjcziybxowkaibqnndcjbsoehtamhspnidjylyisiaewmypfyiqtwlmejkpzlieolfdjnxntonnzfgcqlcfpoxcwqctalwrgwhvqvtrpwemxhirpgizjffqgntsmvzldpjfijdncexbwtxnmbnoykxshkqbounzrewkpqjxocvaufnhunsmsazgibxedtopnccriwcfzeomsrrangufkjfzipkmwfbmkarnyyrgdsooosgqlkzvorrrsaveuoxjeajvbdpgxlcrtqomliphnlehgrzgwujogxteyulphhuhwyoyvcxqatfkboahfqhjgujcaapoyqtsdqfwnijlkknuralezqmcryvkankszmzpgqutojoyzsnyfwsyeqqzrlhzbc"
        )
        == "sooos"
    )

"azwdzwmwcqzgcobeeiphemqbjtxzwkhiqpbrprocbppbxrnsxnwgikiaqutwpftbiinlnpyqstkiqzbggcsdzzjbrkfmhgtnbujzszxsycmvipjtktpebaafycngqasbbhxaeawwmkjcziybxowkaibqnndcjbsoehtamhspnidjylyisiaewmypfyiqtwlmejkpzlieolfdjnxntonnzfgcqlcfpoxcwqctalwrgwhvqvtrpwemxhirpgizjffqgntsmvzldpjfijdncexbwtxnmbnoykxshkqbounzrewkpqjxocvaufnhunsmsazgibxedtopnccriwcfzeomsrrangufkjfzipkmwfbmkarnyyrgdsooosgqlkzvorrrsaveuoxjeajvbdpgxlcrtqomliphnlehgrzgwujogxteyulphhuhwyoyvcxqatfkboahfqhjgujcaapoyqtsdqfwnijlkknuralezqmcryvkankszmzpgqutojoyzsnyfwsyeqqzrlhzbc"
# assert Solution().longestPalindrome("babad") in ("bab", "aba")
# assert Solution().longestPalindrome("cbbd") == "bb"
# assert Solution().longestPalindrome("cabbad") == "abba"
# assert Solution().longestPalindrome("aacabdkacaa") == "aca"
# assert (
#     Solution().longestPalindrome("babaddtattarrattatddetartrateedredividerb")
#     == "ddtattarrattatdd"
# )
