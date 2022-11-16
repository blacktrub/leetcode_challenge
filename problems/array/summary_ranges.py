from typing import List


class Range:
    def __init__(self, start: int) -> None:
        self.start = start
        self.end = start

    def label(self) -> str:
        if self.start == self.end:
            return str(self.start)
        return f"{self.start}->{self.end}"


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        cur = Range(nums[0])
        res = []
        for n in nums[1:]:
            if cur.end + 1 == n:
                cur.end = n
            else:
                res.append(cur)
                cur = Range(n)
        res.append(cur)
        return [x.label() for x in res]


if __name__ == "__main__":
    assert Solution().summaryRanges([1, 2]) == ["1->2"]
