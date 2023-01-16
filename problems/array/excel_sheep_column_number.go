package main

func titleToNumber(columnTitle string) int {
	if len(columnTitle) == 1 {
		return int(columnTitle[0]) - 64
	}
	res := titleToNumber(columnTitle[1:])
	return 26*res + res
}
