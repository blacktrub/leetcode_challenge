package main

func findPeakElement(nums []int) int {
	i := 0
	j := len(nums) - 1

	for i < j {
		m := ((i + j) / 2) + 1
		if m == 0 && nums[m] > nums[m+1] {
			return m
		}

		if m == len(nums)-1 && nums[m] > nums[m-1] {
			return m
		}

		if nums[m] > nums[m-1] && nums[m] > nums[m+1] {
			return m
		}

		if nums[m] < nums[m-1] {
			j = m - 1
		} else {
			i = m + 1
		}
	}

	return i
}
