"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = len(nums1) + len(nums2)
        i, j = 0, 0
        prev, prevprev = 0, 0
        while i < len(nums1) or j < len(nums2):
            if i >= len(nums1):
                prevprev = prev
                prev = nums2[j]
                j += 1
            elif j >= len(nums2):
                prevprev = prev
                prev = nums1[i]
                i += 1
            elif nums1[i] < nums2[j]:
                prevprev = prev
                prev = nums1[i]
                i += 1
            else:
                prevprev = prev
                prev = nums2[j]
                j += 1

            m = l // 2
            if (i + j - 1) == m:
                if l % 2 == 1:
                    return prev
                else:
                    return (prev + prevprev) / 2


if __name__ == "__main__":
    assert Solution().findMedianSortedArrays([1, 3], [2]) == 2.0
    assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5
