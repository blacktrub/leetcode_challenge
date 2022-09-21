from typing import List


class Solution:
    def sumEvenAfterQueries(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        res = []
        sm = sum(x for x in nums if x % 2 == 0)
        for val, i in queries:
            prev = nums[i]
            nums[i] += val
            if prev % 2 == 0:
                sm -= prev
            if nums[i] % 2 == 0:
                sm += nums[i]
            res.append(sm)
        return res


if __name__ == "__main__":
    assert Solution().sumEvenAfterQueries(
        [1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    ) == [8, 6, 2, 4]
