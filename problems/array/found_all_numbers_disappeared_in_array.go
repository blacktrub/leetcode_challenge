package main

func findDisappearedNumbers(nums []int) []int {
	cnt := map[int]int{}

	for i := 0; i < len(nums); i++ {
		cnt[nums[i]]++
	}

	var res []int
	for i := 1; i <= len(nums); i++ {
		_, ok := cnt[i]
		if !ok {
			res = append(res, i)
		}
	}
	return res
}
