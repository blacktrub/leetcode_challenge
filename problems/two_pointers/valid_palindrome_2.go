package main

func validPalindrome(s string) bool {
	var i, j int
	if len(s)%2 == 1 {
		i = len(s) / 2
		j = len(s)/2 + 2
	} else {
		i = len(s) / 2
		j = len(s)/2 + 1
	}
	att := 1
	for i >= 0 && j < len(s) {
		if s[i] != s[j] {
			if att == 0 {
				return false
			}

			if i > 0 && s[i-1] == s[j] {
				i--
			} else if j < len(s)-1 && s[j+1] == s[i] {
				j++
			} else {
				return false
			}
			att--
		} else {
			i--
			j++
		}
	}
	return true
}
