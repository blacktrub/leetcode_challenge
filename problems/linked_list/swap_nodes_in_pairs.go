package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func swapPairs(head *ListNode) *ListNode {
	if head == nil || head != nil && head.Next == nil {
		return head
	}
	dummy := &ListNode{Next: head}
	prev := dummy
	cur := head
	for cur != nil && cur.Next != nil {
		newCur := cur.Next
		prev.Next = newCur
		cur.Next = newCur.Next
		newCur.Next = cur

		prev = cur
		cur = cur.Next
	}

	return dummy.Next
}
