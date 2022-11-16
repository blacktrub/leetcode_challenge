"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
    1 <= n <= 8

TODO: I don't understand the solution
"""


from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def back(x, y):
            if x == y == n:
                res.append("".join(stack))
                return

            if x < n:
                stack.append("(")
                back(x + 1, y)
                stack.pop()

            if x > y:
                stack.append(")")
                back(x, y + 1)
                stack.pop()

        back(0, 0)
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.generateParenthesis(3) == [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()",
    ]
