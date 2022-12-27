package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func getIntersectionNode(headA, headB *ListNode) *ListNode {
	var lenA int
	cur := headA
	for cur != nil {
		lenA++
		cur = cur.Next
	}

	var lenB int
	cur = headB
	for cur != nil {
		lenB++
		cur = cur.Next
	}

	for lenA > lenB {
		lenA--
		headA = headA.Next
	}

	for lenB > lenA {
		lenB--
		headB = headB.Next
	}

	for headA != nil && headB != nil {
		if headA == headB {
			return headA
		}
		headA = headA.Next
		headB = headB.Next
	}

	return nil
}
