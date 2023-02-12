package main

func arrangeCoins(n int) int {
	if n == 1 {
		return n
	}

	l, r := 1, n
	var res int

	for l <= r {
		m := (l + r) / 2
		c := (float32(m)/2)*float32(m) + 1
		if c > float32(n) {
			r = m - 1
		} else {
			l = m + 1
			if m > res {
				res = m
			}
		}
	}

	return res
}
