package main

func FindMaxConsecutiveOnes(nums []int) int {
	skip := -1
	if nums[0] == 0 {
		skip = 0
	}

	var l, r int
	var res int
	for r < len(nums) {
		if nums[r] == 0 {
			if skip >= l {
				l = skip + 1
			}
			skip = r
		}

		if r-l+1 > res {
			res = r - l + 1
		}
		r++
	}
	return res
}
