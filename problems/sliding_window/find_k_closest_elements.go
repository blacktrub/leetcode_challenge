package main

func findClosestElements(arr []int, k int, x int) []int {
	var l, r int = 0, len(arr) - k
	for l < r {
		m := (l + r) / 2
		if x-arr[m] > arr[m+k]-x {
			l = m + 1
		} else {
			r = m
		}
	}
	return arr[l : l+k]
}
