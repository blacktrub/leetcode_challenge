package main

func longestSubarray(nums []int) int {
	l := 0
	for i := 0; i < len(nums); i++ {
		l = i
		if nums[i] == 1 {
			break
		}
	}

	res := 0
	var skip int
	if l == 0 {
		skip = -1
	} else {
		skip = 0
	}

	for r := l; r < len(nums); r++ {
		if nums[r] == 0 {
			if l <= skip {
				l = skip + 1
				skip = r
				continue
			} else {
				skip = r
			}
		}

		cur := r - l + 1
		if l <= skip {
			cur--
		}

		if cur > res {
			res = cur
		}
	}

	if skip == -1 {
		res--
	}

	return res
}
