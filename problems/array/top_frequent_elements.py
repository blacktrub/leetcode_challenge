"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

TODO: there is a more effecient way to do it
"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mem = {}
        for n in nums:
            mem[n] = mem.get(n, 0) + 1

        bucket = []
        for _ in range(len(nums) + 1):
            bucket.append([])

        for key, val in mem.items():
            bucket[val].append(key)

        out = []
        for x in range(len(bucket) - 1, -1, -1):
            item = bucket[x]
            for y in item:
                out.append(y)
                if len(out) == k:
                    return out

        return out


if __name__ == "__main__":
    s = Solution()
    # v = s.topKFrequent([1, 1, 1, 2, 2, 3], 2)
    # assert v == [1, 2], v
    v = s.topKFrequent([1], 1)
    assert v == [1], v
