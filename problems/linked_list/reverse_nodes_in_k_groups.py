"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Constraints:
    The number of nodes in the list is n.
    1 <= k <= n <= 5000
    0 <= Node.val <= 1000

Follow-up: Can you solve the problem in O(1) extra memory space?
"""

from typing import Optional


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[Node], k: int) -> Optional[Node]:
        def reverse(n, next, end):
            if n == end:
                return n

            real = n.next
            n.next = next
            if not real:
                return n
            return reverse(real, n, end)

        dummy = Node()
        fast, slow = head, head
        prev_end = dummy
        while fast:
            c = 1
            while fast.next and c < k:
                fast = fast.next
                c += 1

            if c < k:
                break

            next = fast.next

            end, start = slow, fast
            reverse(slow, next, next)
            prev_end.next = start
            prev_end = end
            slow = fast = next

        return dummy.next


def prepare_nodes(arr):
    dummy = Node()
    head = dummy
    prev = None
    for x in arr:
        head.val = x
        head.next = Node()
        prev = head
        head = head.next
    prev.next = None
    return dummy


if __name__ == "__main__":
    # assert Solution().reverseKGroup(prepare_nodes([1, 2, 3, 4, 5]), 2) == prepare_nodes(
    #     [2, 1, 4, 3, 5]
    # )

    assert Solution().reverseKGroup(prepare_nodes([1, 2, 3, 4, 5]), 3) == prepare_nodes(
        [3, 2, 1, 4, 5]
    )
