package main

func isIsomorphic(s string, t string) bool {
	trns := map[byte]byte{}
	busy := map[byte]int{}
	for i := 0; i < len(s); i++ {
		val, tran := trns[s[i]]
		if tran {
			if val != t[i] {
				return false
			}
		} else {
			_, isBusy := busy[t[i]]
			if isBusy {
				return false
			}
		}

		trns[s[i]] = t[i]
		busy[t[i]] = 1
	}
	return true
}
