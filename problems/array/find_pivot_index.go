package main

func pivotIndex(nums []int) int {
	var total, cur int
	for i := 0; i < len(nums); i++ {
		total += nums[i]
	}

	for i := 0; i < len(nums); i++ {
		if cur == (total-nums[i])/2 && (total-nums[i])%2 == 0 {
			return i
		}
		cur += nums[i]
	}

	return -1
}
