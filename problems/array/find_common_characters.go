package main

func commonChars(words []string) []string {
	var all [26]int
	for _, ch := range words[0] {
		all[int(ch)-97]++
	}

	for i := 1; i < len(words); i++ {
		var arr [26]int
		for _, ch := range words[i] {
			arr[int(ch)-97]++
		}
		for j := 0; j < len(arr); j++ {
			if arr[j] < all[j] {
				all[j] = arr[j]
			}
		}
	}
	res := []string{}
	for i := 0; i < len(all); i++ {
		for j := 0; j < all[i]; j++ {
			res = append(res, string(i+97))
		}
	}
	return res
}
