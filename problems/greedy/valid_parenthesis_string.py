"""
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
The following rules define a valid string:
    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    Any right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "(*)"
Output: true

Example 3:
Input: s = "(*))"
Output: true

Constraints:
    1 <= s.length <= 100
    s[i] is '(', ')' or '*'.
"""


opn = "("
close = ")"


class Solution:
    def checkValidString(self, s: str) -> bool:
        opened = 0
        free = 0
        for i in range(len(s)):
            ch = s[i]
            if ch == opn:
                print("opn", opened)
                if opened > 0 and free > 0:
                    while free > 0 and opened > 0:
                        opened -= 1
                        free -= 1

                opened += 1
            elif ch == "*":
                free += 1
            else:
                if opened <= 0:
                    if free <= 0:
                        return False
                    free -= 1
                    opened += 1
                opened -= 1

        # while opened < 0 and free > 0:
        #     opened += 1
        #     free -= 1
        #
        while opened > 0 and free > 0:
            opened -= 1
            free -= 1

        print(opened, free)
        return opened == 0


if __name__ == "__main__":
    # assert Solution().checkValidString("()") == True
    assert Solution().checkValidString("(*)") == True
    assert Solution().checkValidString("(*))") == True
    assert Solution().checkValidString("((*)()") == True
    assert Solution().checkValidString("((*)") == True
    assert Solution().checkValidString("(*))") == True
    assert (
        Solution().checkValidString(
            "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
        )
        == False
    )
    # assert Solution().checkValidString("(") == False
    # assert (
    #     Solution().checkValidString(
    #         "(((((*(((((*)*(**()))))())((()))))))))((((()*)))))(((**(*)))(*)"
    #     )
    #     == True
    # )
