package main

func merge(l1 *ListNode, l2 *ListNode, add int) *ListNode {
	if l1 == nil && l2 == nil {
		if add != 0 {
			return &ListNode{add, nil}
		} else {
			return nil
		}
	}

	sm := 0 + add
	var newL1 *ListNode
	var newL2 *ListNode
	if l1 != nil {
		sm = sm + l1.Val
		newL1 = l1.Next
	}
	if l2 != nil {
		sm = sm + l2.Val
		newL2 = l2.Next
	}
	newAdd := sm / 10
	sm = sm % 10
	node := &ListNode{sm, nil}
	node.Next = merge(newL1, newL2, newAdd)
	return node
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	return merge(l1, l2, 0)
}
