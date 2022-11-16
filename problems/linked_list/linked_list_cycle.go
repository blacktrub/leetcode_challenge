package main

func hasCycle(head *ListNode) bool {
	if head == nil {
		return false
	}

	slow := head
	fast := head
	for fast != nil {
		slow = slow.Next
		if fast.Next == nil {
			break
		}

		fast = fast.Next.Next

		if slow == fast {
			return true
		}
	}

	return false
}
