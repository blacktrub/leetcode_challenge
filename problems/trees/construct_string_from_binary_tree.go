package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func tree2str(root *TreeNode) string {
	if root == nil {
		return ""
	}
	res := fmt.Sprintf("%d", root.Val)
	if root.Left != nil && root.Right != nil {
		res = res + fmt.Sprintf("(%s)", tree2str(root.Left))
		res = res + fmt.Sprintf("(%s)", tree2str(root.Right))
	} else if root.Left == nil && root.Right != nil {
		res = res + "()"
		res = res + fmt.Sprintf("(%s)", tree2str(root.Right))
	} else if root.Left != nil {
		res = res + fmt.Sprintf("(%s)", tree2str(root.Left))
	}
	return string(res)
}
