"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5

Constraints:
    -1000 <= a, b <= 1000
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        def to_tc(x):
            return x & 0xFFFF_FFFF

        def sum(a, b):
            if b == 0:
                return a
            b, a = to_tc((a & b) << 1), a ^ b
            return sum(a, b)

        res = sum(to_tc(a), to_tc(b))
        if res & 0x8000_0000:
            return (res ^ 0xFFFF_FFFF) ^ -1
        return res


if __name__ == "__main__":
    assert Solution().getSum(1, 2) == 3
    assert Solution().getSum(-1, -2) == -3
    assert Solution().getSum(10, 11) == 21
    assert Solution().getSum(11, -5) == 6
    assert Solution().getSum(1, -5) == -4
