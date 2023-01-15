package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findSum(root *TreeNode, t, c, p int) bool {
	if root == nil {
		return c == t && p > 1
	}
	c += root.Val
	if findSum(root.Left, t, c, p+1) {
		return true
	}
	if findSum(root.Right, t, c, p+1) {
		return true
	}
	return false
}

func hasPathSum(root *TreeNode, targetSum int) bool {
	if root == nil {
		return false
	}
	if root.Left == nil && root.Right == nil {
		return root.Val == targetSum
	}
	return findSum(root, targetSum, 0, 0)
}
