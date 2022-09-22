class Solution:
    def reverseWords(self, s: str) -> str:
        i, j = 0, 1
        res = ""
        while i < j and j < len(s):
            while j < len(s) and s[j] != " ":
                j += 1

            j -= 1
            tmp = j
            while j >= i and s[j] != " ":
                res += s[j]
                j -= 1

            j = tmp + 2
            i = j - 1
            res += " "

        return res.strip()


if __name__ == "__main__":
    assert (
        Solution().reverseWords("Let's take LeetCode contest")
        == "s'teL ekat edoCteeL tsetnoc"
    )
