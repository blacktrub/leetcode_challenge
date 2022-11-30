package main

func numSquares(n int) int {
	dp := make([]int, n+1)
	for i := 0; i < len(dp); i++ {
		dp[i] = n
	}

	dp[0] = 0
	for i := 1; i < n+1; i++ {
		for j := 1; j < i+1; j++ {
			s := j * j
			if i-s < 0 {
				break
			}

			if 1+dp[i-s] < dp[i] {
				dp[i] = 1 + dp[i-s]
			}

		}
	}

	return dp[len(dp)-1]
}
