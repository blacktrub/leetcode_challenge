package main

func nextGreaterElement(nums1 []int, nums2 []int) []int {
	greater := map[int]int{}
	for i := 0; i < len(nums1); i++ {
		greater[nums1[i]] = -1
	}

	stack := []int{}
	for i := 0; i < len(nums2); i++ {
		for len(stack) > 0 && stack[len(stack)-1] < nums2[i] {
			p := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			_, ok := greater[p]
			if ok {
				greater[p] = nums2[i]
			}
		}
		stack = append(stack, nums2[i])
	}

	res := []int{}
	for i := 0; i < len(nums1); i++ {
		res = append(res, greater[nums1[i]])
	}
	return res

}
