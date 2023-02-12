package main

func islandPerimeter(grid [][]int) int {
	rows := len(grid)
	cols := len(grid[0])

	var res int
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if grid[i][j] == 1 {
				q := []int{grid[i][j]}
				for len(q) > 0 {
					cell := q[0]
					q = q[1:]

				}
			}

		}
	}
	return res
}
