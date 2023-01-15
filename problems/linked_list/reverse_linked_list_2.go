package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverse(head *ListNode, next *ListNode, end *ListNode) *ListNode {
	realNext := head.Next
	head.Next = next

	if head == end {
		return head
	}
	return reverse(realNext, head, end)
}

func reverseBetween(head *ListNode, left int, right int) *ListNode {
	if head == nil || left == right {
		return head
	}
	dummy := &ListNode{Next: head}

	prevLeft := dummy
	leftNode := head
	var i int
	for i < left-1 {
		i++
		prevLeft = leftNode
		leftNode = leftNode.Next
	}

	rightNode := leftNode
	for i < right-1 {
		i++
		rightNode = rightNode.Next
	}

	prevLeft.Next = reverse(leftNode, rightNode.Next, rightNode)
	return dummy.Next
}
