"""
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

Example 1:
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:
Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]

Constraints:
    1 <= arr.length <= 104
    0 <= arr[i] <= 9

TODO there is a faster solution - https://leetcode.com/problems/duplicate-zeros/solution/
"""


from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        while i < len(arr) - 1:
            x = arr[i]
            if x == 0:
                c = len(arr) - 1
                while c > i:
                    arr[c] = arr[c - 1]
                    c -= 1

                arr[i + 1] = 0
                i += 2
                continue

            i += 1


if __name__ == "__main__":
    s = Solution()
    arr = [1, 0, 2, 3, 0, 4, 5, 0]
    s.duplicateZeros(arr)
    assert arr == [1, 0, 0, 2, 3, 0, 0, 4], arr
    arr = [1, 2, 3]
    s.duplicateZeros(arr)
    assert arr == [1, 2, 3]
