package main

func countPalindromicSubsequence(s string) int {
	cnt := map[rune][]int{}
	for i, ch := range s {
		cnt[ch] = append(cnt[ch], i)
	}

	res := map[string]bool{}
	for key := range cnt {
		if len(cnt[key]) < 2 {
			continue
		}

		var i int
		j := len(cnt[key]) - 1
		if cnt[key][j]-cnt[key][i]-1 < 1 {
			continue
		}

		for k := cnt[key][i] + 1; k < cnt[key][j]; k++ {
			res[string(s[cnt[key][i]])+string(s[k])+string(s[cnt[key][j]])] = true
		}

	}
	return len(res)
}
