package main

func interchangeableRectangles(rectangles [][]int) int64 {
	res := map[float64][]int64{}
	for i := 0; i < len(rectangles); i++ {
		ratio := float64(rectangles[i][0]) / float64(rectangles[i][1])

		if len(res[ratio]) == 0 {
			res[ratio] = append(res[ratio], 0)
			continue
		}

		cur := res[ratio][len(res[ratio])-1]
		res[ratio] = append(res[ratio], cur+int64(len(res[ratio])))
	}
	var out int64
	for key := range res {
		out += res[key][len(res[key])-1]
	}
	return out
}
