package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func merge(left, right *TreeNode) *TreeNode {
	node := right
	if node.Left == nil {
		node.Left = left
	} else {
		cur := node.Left
		for cur.Left != nil {
			cur = cur.Left
		}

		cur.Left = left
	}

	return node
}

func deleteNode(root *TreeNode, key int) *TreeNode {
	dummy := TreeNode{Left: root}

	cur := root
	var node, prev *TreeNode
	for cur != nil {
		if cur.Val == key {
			node = cur
			break
		}

		prev = cur
		if cur.Val > key {
			cur = cur.Left
		} else {
			cur = cur.Right
		}
	}

	if node == nil {
		return dummy.Left
	}

	if node.Right != nil {
		*node = *merge(node.Left, node.Right)
	} else if node.Left != nil {
		*node = *merge(node.Right, node.Left)
	} else if prev != nil {
		if prev.Left == node {
			prev.Left = nil
		} else {
			prev.Right = nil
		}
	} else {
		return nil
	}

	return dummy.Left
}
