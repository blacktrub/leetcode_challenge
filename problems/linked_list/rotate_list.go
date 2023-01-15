package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func rotateRight(head *ListNode, k int) *ListNode {
	if k == 0 || head == nil {
		return head
	}

	dummy := &ListNode{Next: head}
	var l int
	cur := head
	for cur != nil {
		l++
		cur = cur.Next
	}

	k = k % l
	if k == 0 {
		return head
	}

	var i int
	cur = head
	prev := dummy
	for i < (l - k) {
		i++
		prev = cur
		cur = cur.Next
	}

	end := head
	for end.Next != nil {
		end = end.Next
	}

	prev.Next = nil
	end.Next = dummy.Next
	dummy.Next = cur
	return dummy.Next
}
