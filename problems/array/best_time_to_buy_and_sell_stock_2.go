package main

func maxProfit(prices []int) int {
	res := []int{0}
	var i int
	var j int = 1
	for j < len(prices) && i < j {
		d := prices[j] - prices[i]
		if d > res[len(res)-1] {
			res[len(res)-1] = d
		}

		if d < (prices[j-1] - prices[i]) {
			i = j
			res = append(res, 0)
		}

		j++
	}
	var t int
	for i := 0; i < len(res); i++ {
		t += res[i]
	}
	return t
}
