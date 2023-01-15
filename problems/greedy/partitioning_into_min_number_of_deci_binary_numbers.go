package main

import (
	"strconv"
)

// TODO: doesn't work
func minPartitions(n string) int {
	if n == "0" {
		return 0
	}

	num := 1
	for i := 0; i < len(n); i++ {
		num = num*10 + 1
	}

	nn, _ := strconv.Atoi(n)
	if num > nn {
		num--
	}

	return nn/num + minPartitions(strconv.Itoa(nn-num*(nn/num)))
}
