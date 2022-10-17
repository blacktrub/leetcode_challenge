"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    1 <= k <= nums.length
"""

from typing import List
from heapq import heappop, heappush


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def convert_for_heap(n):
            if n > 0:
                n = -n
            else:
                n = abs(n)
            return n

        heap = []
        l, r = 0, k - 1
        res = []
        for x in range(l, r + 1):
            n = nums[x]
            heappush(heap, (convert_for_heap(n), x))

        while r < len(nums):
            while True:
                _, i = heap[0]
                if i >= l:
                    break
                heappop(heap)

            higest, _ = heap[0]
            res.append(convert_for_heap(higest))

            l += 1
            r += 1

            if r > len(nums) - 1:
                break

            heappush(heap, (convert_for_heap(nums[r]), r))

        return res


if __name__ == "__main__":
    assert Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [
        3,
        3,
        5,
        5,
        6,
        7,
    ]
    assert Solution().maxSlidingWindow([1], 1) == [1]
