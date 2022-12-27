package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
	if head == nil {
		return head
	}

	dummy := &ListNode{Next: head, Val: -101}
	prev := dummy

	for head != nil {
		if prev.Val == head.Val {
			prev.Next = head.Next
			head = head.Next
		} else {
			prev = head
			head = head.Next
		}

	}
	return dummy.Next
}
