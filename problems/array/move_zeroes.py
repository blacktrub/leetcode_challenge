from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        while l < len(nums) and nums[l] != 0:
            l += 1

        for r in range(l + 1, len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                while l < len(nums) and nums[l] != 0:
                    l += 1

        return nums


if __name__ == "__main__":
    assert Solution().moveZeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
