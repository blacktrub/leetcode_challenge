package main

func z(pattern string, text string) []int {
	s := pattern + "#" + text
	res := make([]int, len(s))
	var left, right int
	for i := 1; i < len(s); i++ {
		m := res[i-left]
		if right-i < m {
			m = right - i
		}

		if m > 0 {
			res[i] = m
		}

		for i+res[i] < len(s) && s[res[i]] == s[res[i]+i] {
			res[i]++
		}

		if i+res[i] > right {
			left = i
			right = i + res[i]
		}

	}
	return res
}

func strStr(haystack string, needle string) int {
	res := z(needle, haystack)
	for i := 0; i < len(res); i++ {
		if res[i] == len(needle) {
			return i - len(needle) - 1
		}
	}
	return -1
}
