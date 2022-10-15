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


class Solution:
    def checkValidString(self, s: str) -> bool:
        open_string = chr(40)
        left_min, left_max = 0, 0
        for x in range(len(s)):
            if s[x] == open_string:
                left_min += 1
                left_max += 1
            elif s[x] == "*":
                left_min = max(0, left_min - 1)
                left_max += 1
            else:
                left_min = max(0, left_min - 1)
                left_max -= 1

            if left_max < 0:
                return False

        return left_min == 0 or left_max == 0


if __name__ == "__main__":
    assert Solution().checkValidString("()") == True
    assert Solution().checkValidString("(*)") == True
    assert Solution().checkValidString("(*))") == True
    assert Solution().checkValidString("((*)") == True
    assert (
        Solution().checkValidString(
            "(((()))())))*))())()(**(((())(()(*()((((())))*())(())*(*(()(*)))()*())**((()(()))())(*(*))*))())"
        )
        == False
    )
