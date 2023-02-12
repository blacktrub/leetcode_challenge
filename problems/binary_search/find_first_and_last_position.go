package main

// TODO: there is a better way to find the first and the last element of the sequence
func searchRange(nums []int, target int) []int {
	i := 0
	j := len(nums) - 1
	for i <= j {
		m := (i + j) / 2
		if nums[m] == target {
			for nums[i] != target {
				i++
			}
			for nums[j] != target {
				j--
			}
			return []int{i, j}
		}

		if nums[m] > target {
			j = m - 1
		} else {
			i = m + 1
		}
	}
	return []int{-1, -1}
}
