package main

func majorityElement(nums []int) int {
	res := map[int]int{}
	for _, n := range nums {
		v := res[n]
		res[n] = v + 1
		if res[n] >= len(nums)/2 {
			return n
		}
	}
}
