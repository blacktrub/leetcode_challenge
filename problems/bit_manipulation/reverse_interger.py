"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Constraints:
    -231 <= x <= 231 - 1
"""


class Solution:
    def reverse(self, x: int) -> int:
        min_32 = -(2 ** 31)
        max_32 = (2 ** 31) - 1

        def reverse_int(x, y, add):
            if add < 0 and (y * add) < -(abs(min_32) // 10):
                return 0

            if add > 0 and y > (max_32 // 10):
                return 0

            if x < 10 and x > -10:
                return (y * 10 + x) * add

            return reverse_int(x // 10, y * 10 + (x % 10), add)

        return reverse_int(abs(x), 0, 1 if x > 0 else -1)


if __name__ == "__main__":
    assert Solution().reverse(123) == 321
    assert Solution().reverse(-123) == -321
    assert Solution().reverse(120) == 21
    assert Solution().reverse(1534236469) == 0
    assert Solution().reverse(-1563847412) == 0
