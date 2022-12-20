package main

func majorityElement(nums []int) int {
	cnt := map[int]int{}
	for i := 0; i < len(nums); i++ {
		cnt[nums[i]]++
	}
	var res int = nums[0]
	for k, v := range cnt {
		if v > cnt[res] {
			res = k
		}
	}
	return res
}
