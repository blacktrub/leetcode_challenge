package main

func reverse(head *ListNode, next *ListNode) *ListNode {
	realNext := head.Next
	head.Next = next
	if realNext == nil {
		return head
	}

	return reverse(realNext, head)
}

func reverseList(head *ListNode) *ListNode {
	return reverse(head, nil)
}
