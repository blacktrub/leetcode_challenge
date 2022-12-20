package main

func leastBricks(wall [][]int) int {
	cnt := map[int]int{}
	var res int
	for i := 0; i < len(wall); i++ {
		var p int
		for j := 0; j < len(wall[i])-1; j++ {
			p += wall[i][j]
			cnt[p]++
			if cnt[p] > res {
				res = cnt[p]
			}
		}
	}
	return len(wall) - res
}
