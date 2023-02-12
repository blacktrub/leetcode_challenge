package main

func minFlipsMonoIncr(s string) int {
	var res int = len(s)
	var total_zeros int
	for i := len(s) - 1; i >= 0; i-- {
		if s[i] == '0' {
			total_zeros++
		}
	}

	var ones int
	var zeros int
	for i := 0; i < len(s); i++ {
		if i > 0 && s[i-1] == '1' {
			ones++
		}

		if i > 0 && s[i-1] == '0' {
			zeros++
		}

		flips := ones + (total_zeros - zeros)
		if flips < res {
			res = flips
		}
	}

	if ones < res {
		res = ones
	}

	return res
}
