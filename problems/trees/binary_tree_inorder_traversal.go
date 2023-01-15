package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// func inorderTraversal(root *TreeNode) []int {
// 	if root == nil {
// 		return []int{}
// 	}
//
// 	res := inorderTraversal(root.Left)
// 	res = append(res, root.Val)
// 	res = append(res, inorderTraversal(root.Right)...)
// 	return res
// }

func inorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}

	stack := []*TreeNode{root}
	res := []int{}
	for len(stack) > 0 {
		node := stack[len(stack)-1]
		if node.Left != nil {
			stack = append(stack, node.Left)
			continue
		}
		res = append(res, node.Val)
		stack = stack[:len(stack)-1]
		if node.Right != nil {
			res = append(res, node.Right.Val)
		}
	}
	return res
}
