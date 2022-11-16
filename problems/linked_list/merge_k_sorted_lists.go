package main

import (
	"container/heap"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

type NodeHeap []int

func (h NodeHeap) Len() int {
	return len(h)
}

func (h NodeHeap) Less(i, j int) bool {
	return h[i] < h[j]
}

func (h NodeHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *NodeHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *NodeHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func mergeKLists(lists []*ListNode) *ListNode {
	h := &NodeHeap{}
	for i := 0; i < len(lists); i++ {
		head := lists[i]
		for head != nil {
			heap.Push(h, head.Val)
			head = head.Next
		}
	}

	dummy := &ListNode{0, nil}
	head := dummy
	for h.Len() > 0 {
		x := heap.Pop(h).(int)
		n := &ListNode{x, nil}
		head.Next = n
		head = n
	}

	return dummy.Next
}
