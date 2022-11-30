package main

func subarraySum(nums []int, k int) int {
	var prefix int
	var res int
	mem := map[int]int{}
	mem[0] = 1

	for i := 0; i < len(nums); i++ {
		prefix = prefix + nums[i]
		d := prefix - k
		count, ok := mem[d]
		if ok {
			res = res + count
		}

		cur, ok := mem[prefix]
		if !ok {
			mem[prefix] = 1
		} else {
			mem[prefix] = cur + 1
		}
	}
	return res
}
