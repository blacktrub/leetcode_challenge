"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Constraints:
    -100.0 < x < 100.0
    -231 <= n <= 231-1
    n is an integer.
    -104 <= xn <= 104
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0

        if n == 0:
            return 1

        def pow(x, n):
            if n == 0:
                return 1

            add = x if n % 2 != 0 else 1
            x = pow(x, n // 2)
            return x * x * add

        if n < 0:
            return 1 / pow(x, abs(n))
        else:
            return pow(x, n)


if __name__ == "__main__":
    assert Solution().myPow(2, 10) == 1024
    assert Solution().myPow(2, -2) == 0.25
    assert Solution().myPow(2.1, 3) == 9.26100
    assert Solution().myPow(0.00001, 2147483647) == 0
