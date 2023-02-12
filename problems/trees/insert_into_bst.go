package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func find(root *TreeNode, val int) *TreeNode {

}

func insertIntoBST(root *TreeNode, val int) *TreeNode {
	dummy := TreeNode{Left: root}
	cur := root
	for cur != nil {
		if cur.Val > val && (cur.Left == nil || cur.Left.Val < val) {
			if cur.Left != nil && cur.Left.Right != nil && cur.Left.Right.Val > val {
				cur = cur.Left.Right
				continue
			}

			break
		}

		if cur.Val < val && (cur.Right == nil || cur.Right.Val > val) {
			if cur.Right != nil && cur.Right.Left != nil && cur.Right.Left.Val < val {
				cur = cur.Right.Left
				continue
			}

			break
		}

		if cur.Val > val {
			cur = cur.Left
		} else {
			cur = cur.Right
		}
	}
	if cur.Val > val {
		node := &TreeNode{Val: val}
		if cur.Left == nil {
			cur.Left = node
		} else {
			node.Left = cur.Left
			cur.Left = node
		}
	} else {
		node := &TreeNode{Val: val}
		if cur.Right == nil {
			cur.Right = node
		} else {
			node.Right = cur.Left
			cur.Right = node
		}
	}
	return dummy.Left
}
