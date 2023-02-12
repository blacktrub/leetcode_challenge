package main

func numTrees(n int) int {
	dp := make([]int, n+1)
	dp[0] = 1
	dp[1] = 1

	for i := 2; i <= n; i++ {
		for j := i - 1; j >= 0; j-- {
			dp[i] += dp[j] * dp[i-1-j]
		}
	}
	return dp[n]
}
