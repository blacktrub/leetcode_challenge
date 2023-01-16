package main

func romanToInt(s string) int {
	ch_to_int := map[string]int{
		"I":  1,
		"IV": 4,
		"IX": 9,
		"V":  5,
		"X":  10,
		"XL": 40,
		"XC": 90,
		"L":  50,
		"C":  100,
		"CD": 400,
		"CM": 900,
		"D":  500,
		"M":  1000,
	}
	var res int
	var prev string

	for _, ch := range s {
		if prev != "" {
			double, ok := ch_to_int[prev+string(ch)]
			if ok {
				res -= ch_to_int[prev]
				res += double
				prev = string(ch)
				continue
			}
		}

		res += ch_to_int[string(ch)]
		prev = string(ch)
	}
	return res

}
