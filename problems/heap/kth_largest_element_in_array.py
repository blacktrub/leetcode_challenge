"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
You must solve it in O(n) time complexity.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
    1 <= k <= nums.length <= 105
    -104 <= nums[i] <= 104
"""

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(left, right):
            p = right
            cur = left
            for x in range(left, right):
                pivot = nums[p]
                if nums[x] <= pivot:
                    nums[cur], nums[x] = nums[x], nums[cur]
                    cur += 1

            nums[cur], nums[p] = nums[p], nums[cur]
            if len(nums) - k == cur:
                return nums[cur]

            if len(nums) - k > cur:
                return quick_select(cur + 1, right)
            else:
                return quick_select(left, cur - 1)

        return quick_select(0, len(nums) - 1)


if __name__ == "__main__":
    s = Solution()
    assert s.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert s.findKthLargest([1, 2, 4, 5, 6, 1, 2, 3], 1) == 6
    assert s.findKthLargest([3, 2, 1, 5, 6, 4], 3) == 4
    assert s.findKthLargest([3, 2, 1, 5, 6, 4], 5) == 2
