from typing import List
import collections


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            return self.intersect(nums2, nums2)

        first = collections.defaultdict(int)
        for x in nums1:
            first[x] += 1

        res = []
        for x in nums2:
            if x in first and first[x] > 0:
                first[x] -= 1
                res.append(x)

        return res


if __name__ == "__main__":
    assert Solution().intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
