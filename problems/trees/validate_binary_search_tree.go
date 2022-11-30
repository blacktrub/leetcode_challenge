package main

import "math"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isValidSubTree(root *TreeNode, left, right int) bool {
	if root == nil {
		return true
	}

	var res bool = true
	res = root.Val > left && root.Val < right
	res = res && isValidSubTree(root.Left, left, root.Val)
	res = res && isValidSubTree(root.Right, root.Val, right)
	return res
}

func isValidBST(root *TreeNode) bool {
	return isValidSubTree(root, math.MinInt64, math.MaxInt64)
}
