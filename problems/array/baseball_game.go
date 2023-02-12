package main

import (
	"strconv"
)

func calPoints(operations []string) int {
	stack := []int{}
	for i := 0; i < len(operations); i++ {
		cur := operations[i]
		n, ok := strconv.Atoi(cur)
		if ok == nil {
			stack = append(stack, n)
			continue
		}

		switch cur {
		case "+":
			one := stack[len(stack)-1]
			two := stack[len(stack)-2]
			stack = append(stack, (one + two))
		case "D":
			stack = append(stack, stack[len(stack)-1]*2)
		case "C":
			stack = stack[:len(stack)-1]
		}

	}

	var res int
	for i := 0; i < len(stack); i++ {
		res += stack[i]
	}
	return res
}
