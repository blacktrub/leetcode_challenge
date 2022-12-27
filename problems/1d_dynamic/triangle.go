package main

func minimumTotal(triangle [][]int) int {
	dp := [][]int{}
	for i := 0; i < len(triangle); i++ {
		dp = append(dp, make([]int, len(triangle[i])))
	}
	dp[0][0] = triangle[0][0]

	for i := 1; i < len(triangle); i++ {
		for j := 0; j < len(triangle[i]); j++ {
			var m int
			if j > 0 {
				m = dp[i-1][j-1]
			} else {
				m = dp[i-1][j]
			}

			if j < len(triangle[i-1]) && dp[i-1][j] < m {
				m = dp[i-1][j]
			}
			dp[i][j] = m + triangle[i][j]
		}
	}

	var res int = dp[len(dp)-1][0]
	for i := 0; i < len(dp[len(dp)-1]); i++ {
		p := dp[len(dp)-1][i]
		if p < res {
			res = p
		}

	}

	return res
}
