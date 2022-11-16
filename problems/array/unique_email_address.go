package main

import "strings"

type Email struct {
	local  string
	domain string
}

func numUniqueEmails(emails []string) int {
	res := map[Email]int{}
	for i := 0; i < len(emails); i++ {
		email := emails[i]
		parts := strings.SplitN(email, "@", 2)
		local := parts[0]
		var realLocal string
		for j := 0; j < len(local); j++ {
			if string(local[j]) == "+" {
				break
			}
			if string(local[j]) == "." {
				continue
			}

			realLocal = realLocal + string(local[j])
		}

		domain := parts[1]
		e := Email{realLocal, domain}
		_, ok := res[e]
		if ok {
			continue
		}
		res[e] = 1

	}
	return len(res)
}
