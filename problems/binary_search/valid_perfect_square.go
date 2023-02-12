package main

func isPerfectSquare(num int) bool {
	i, j := 1, num
	for i <= j {
		m := (i + j) / 2
		if m*m == num {
			return true
		}

		if m*m > num {
			j = m - 1
		} else {
			i = m + 1
		}
	}

	return false
}
