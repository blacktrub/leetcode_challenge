package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeElements(head *ListNode, val int) *ListNode {
	if head == nil {
		return head
	}

	dummy := ListNode{Next: head}
	prev := &dummy
	cur := head
	for cur != nil {
		if cur.Val == val {
			prev.Next = cur.Next
			cur = cur.Next
		} else {
			prev = cur
			cur = cur.Next
		}
	}
	return dummy.Next
}
