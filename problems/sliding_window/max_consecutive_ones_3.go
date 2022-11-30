package main

func longestOnes(nums []int, k int) int {
	var l, p, res int
	for r := 0; r < len(nums); r++ {
		p += nums[r]
		for (r-l+1)-p > k {
			p -= nums[l]
			l++
		}

		if (r - l + 1) > res {
			res = (r - l + 1)
		}

	}
	return res

}
