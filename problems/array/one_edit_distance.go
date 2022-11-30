package main

func IsOneEditDistance(s string, t string) bool {
	if len(t) > len(s) {
		return IsOneEditDistance(t, s)
	}

	if len(s)-len(t) > 1 {
		return false
	}

	shift := len(s) - len(t)
	var i, j int
	var d int
	for i < len(s) && j < len(t) {
		if d > 1 {
			return false
		}

		if s[i] != t[j] {
			d++
			if shift > 0 {
				i++
				shift--
				continue
			}
		}
		i++
		j++
	}

	if shift > 0 {
		d++
	}
	return d == 1
}
