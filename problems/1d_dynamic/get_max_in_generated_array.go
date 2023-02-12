package main

func getMaximumGenerated(n int) int {
	if n < 2 {
		return n
	}
	arr := make([]int, n+1)
	arr[0] = 0
	arr[1] = 1

	var res int
	for i := 1; i < n+1; i++ {
		if 2*i <= n {
			arr[2*i] = arr[i]
			if arr[i] > res {
				res = arr[i]
			}
		}

		if 2*i+1 <= n {
			arr[2*i+1] = arr[i] + arr[i+1]
			if arr[2*i+1] > res {
				res = arr[2*i+1]
			}
		}
	}
	return res
}
