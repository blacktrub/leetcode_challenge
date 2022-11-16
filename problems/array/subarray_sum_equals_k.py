from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        pref = 0
        mem = defaultdict(int)
        mem[0] = 1
        for x in nums:
            pref += x
            if pref - k in mem:
                res += mem[pref - k]

            mem[pref] += 1

        return res


if __name__ == "__main__":
    assert Solution().subarraySum([1, 1, 1], k=2) == 2
    assert Solution().subarraySum([1, 2, 3], k=3) == 2
