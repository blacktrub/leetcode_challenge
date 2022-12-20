package main

func maxNumberOfBalloons(text string) int {
	cnt := map[rune]int{}
	for _, s := range text {
		cnt[s]++
	}

	// balloon
	bal := map[rune]int{
		'b': 1,
		'a': 1,
		'l': 2,
		'o': 2,
		'n': 1,
	}
	var res int
	for {
		for key := range bal {
			need := bal[key]
			cur, ok := cnt[key]
			if !ok {
				return res
			}

			if cur < need {
				return res
			}
			cnt[key] -= need
		}
		res++
	}
}
