"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:
    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in non-decreasing order.
 
Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

Tags: Merge Sort
"""


from typing import List


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left_array = merge_sort(arr[:mid])
    right_array = merge_sort(arr[mid:])

    i = j = k = 0
    while i < len(left_array) and j < len(right_array):
        l, r = left_array[i], right_array[j]
        if l < r:
            arr[k] = l
            i += 1
        else:
            arr[k] = r
            j += 1
        k += 1

    while i < len(left_array):
        l = left_array[i]
        arr[k] = l
        i += 1
        k += 1

    while j < len(right_array):
        r = right_array[j]
        arr[k] = r
        j += 1
        k += 1

    return arr


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        return merge_sort(nums)


if __name__ == "__main__":
    s = Solution()
    assert s.sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert s.sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
