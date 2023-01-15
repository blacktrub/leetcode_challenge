package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func createTree(nums []int, i, j int) *TreeNode {
	if i == j {
		return nil
	}
	m := (i + j) / 2
	node := &TreeNode{Val: nums[m]}
	node.Right = createTree(nums, m+1, j)
	node.Left = createTree(nums, i, m)
	return node
}

func sortedArrayToBST(nums []int) *TreeNode {
	return createTree(nums, 0, len(nums))
}
