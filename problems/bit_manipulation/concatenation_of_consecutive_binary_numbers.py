class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = ""
        for x in range(1, n + 1):
            res += bin(x)[2:]

        return int(res, 2) % ((10 ** 9) + 7)


if __name__ == "__main__":
    assert Solution().concatenatedBinary(3) == 27
