package main

func removeDuplicates(nums []int) int {
	if len(nums) == 1 {
		return 1
	}

	slow := 1
	fast := 1

	for fast < len(nums) {
		if nums[slow] <= nums[slow-1] {
			for fast < len(nums) && nums[fast] <= nums[slow-1] {
				fast++
			}
			if fast >= len(nums) {
				break
			}
			nums[slow] = nums[fast]
		}
		slow++
		fast++
	}

	return slow
}
