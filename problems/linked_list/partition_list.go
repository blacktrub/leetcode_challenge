package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func partition(head *ListNode, x int) *ListNode {
	dummy := &ListNode{Next: head}

	last := head
	cur := head
	for cur != nil {
		if cur.Val < x {
			last = cur
		}
		cur = cur.Next
	}

	tail := last
	prev := dummy
	cur = head
	for cur != last {
		next := cur.Next

		if cur.Val >= x {
			prev.Next = next
			cur.Next = tail.Next
			tail.Next = cur
			tail = cur
			cur = next
		} else {
			prev = cur
			cur = next
		}

	}

	return dummy.Next
}
