package main

/**
 * @param points: n points on a 2D plane
 * @return: if there is such a line parallel to y-axis that reflect the given points
 */
func IsReflected(points [][]int) bool {
	if len(points) == 0 {
		return true
	}

	left := points[0]
	right := points[0]
	all := map[[2]float64]int{}
	for i := 0; i < len(points); i++ {
		cur := points[i]
		if cur[0] < left[0] {
			left = cur
		}

		if cur[0] > right[0] {
			right = cur
		}

		point := [2]float64{float64(cur[0]), float64(cur[1])}
		all[point] = 1
	}

	line := (float64(left[0]) + float64(right[0])) / 2
	for k, _ := range all {
		var p float64
		var scnd [2]float64
		if line > k[0] {
			p = line - k[0]
			scnd = [2]float64{k[0] + (p * 2), k[1]}
		} else {
			p = k[0] - line
			scnd = [2]float64{k[0] - (p * 2), k[1]}
		}

		_, ok := all[scnd]
		if !ok {
			return false
		}
		all[k] = 0
		all[scnd] = 0
	}

	for k, v := range all {
		if v == 0 {
			delete(all, k)
		}
	}

	return len(all) == 0
}
