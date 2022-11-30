package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseLinkedList(head *ListNode, next *ListNode) *ListNode {
	realNext := head.Next
	head.Next = next
	if realNext == nil {
		return head
	}
	return reverseLinkedList(realNext, head)
}

func isPalindrome(head *ListNode) bool {
	fast := head
	l := 0
	for fast != nil {
		fast = fast.Next
		l++
	}

	slow := head
	for i := 0; i < l/2; i++ {
		slow = slow.Next
	}

	if l%2 == 1 {
		slow = slow.Next
	}

	if slow == nil {
		return true
	}

	fast = reverseLinkedList(slow, nil)
	slow = head
	for i := l / 2; i > 0; i-- {
		if fast.Val != slow.Val {
			return false
		}
		fast = fast.Next
		slow = slow.Next
	}

	return true
}
