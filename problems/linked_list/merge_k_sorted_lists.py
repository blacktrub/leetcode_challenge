"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
    k == lists.length
    0 <= k <= 104
    0 <= lists[i].length <= 500
    -104 <= lists[i][j] <= 104
    lists[i] is sorted in ascending order.
    The sum of lists[i].length will not exceed 104.
"""

from typing import Optional, List
from heapq import heappop, heappush


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[Node]]) -> Optional[Node]:
        heap = []
        for node in lists:
            while node:
                heappush(heap, node.val)
                node = node.next

        dummy = Node()
        head = dummy
        while heap:
            head.next = Node(heappop(heap))
            head = head.next

        return dummy.next


if __name__ == "__main__":
    assert Solution().mergeKLists([Node(1, Node(4)), Node(1, Node(3)), Node(2)]) == [
        1,
        1,
        2,
        3,
        4,
    ]
    assert Solution().mergeKLists([None, Node(1)]) == [1]
