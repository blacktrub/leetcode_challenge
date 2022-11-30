package main

func searchRange(nums []int, target int) []int {
	i := 0
	j := len(nums) - 1
	for i <= j {
		m := (j - i + 1) / 2
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
			i = m + 1
		} else {
			j = m - 1
		}
	}
	return []int{-1, -1}
}

// [1,2,3]
// t = 3
// i = 0 j = 2
// m = 1
// nums[m] = 2
// 2 > t
