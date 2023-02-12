package main

func intersect(nums1 []int, nums2 []int) []int {
	mem := make(map[int]int)
	for _, n := range nums1 {
		mem[n]++
	}

	res := []int{}
	for _, n := range nums2 {
		c, ok := mem[n]
		if ok == true && c > 0 {
			mem[n]--
			res = append(res, n)
		}
	}
	return res
}
