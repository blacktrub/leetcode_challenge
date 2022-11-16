package main

func findMin(arr []int) int {
	m := arr[0]
	for i := 0; i < len(arr); i++ {
		if arr[i] < m {
			m = arr[i]
		}
	}
	return m
}

func maxDistToClosest(seats []int) int {

	left := make([]int, len(seats))
	right := make([]int, len(seats))

	var prev int
	if seats[0] == 1 {
		prev = 0
	} else {
		prev = -1
	}

	for i := 0; i < len(seats); i++ {
		if seats[i] == 1 {
			prev = i
		}

		left[i] = prev
	}

	if seats[len(seats)-1] == 1 {
		prev = len(seats) - 1
	} else {
		prev = -1
	}
	for i := len(seats) - 1; i >= 0; i-- {
		if seats[i] == 1 {
			prev = i
		}
		right[i] = prev
	}

	res := 0
	for i := 0; i < len(seats); i++ {
		choices := []int{}
		if left[i] != -1 {
			choices = append(choices, i-left[i])
		}

		if right[i] != -1 {
			choices = append(choices, right[i]-i)
		}

		m := findMin(choices)
		if m > res {
			res = m
		}
	}

	return res
}
