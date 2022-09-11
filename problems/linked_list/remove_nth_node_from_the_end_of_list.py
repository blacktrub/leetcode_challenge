"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz

Follow up: Could you do this in one pass?
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)


# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         if not head:
#             return head
#
#         if not head.next:
#             return
#
#         def remove_tail(head, prev):
#             if not head:
#                 return 0, head
#
#             tail, tail_head = remove_tail(head.next, head)
#             count = 1 + tail
#             if count == n:
#                 if prev:
#                     prev.next = tail_head
#                 else:
#                     head = tail_head
#             return count, head
#
#         _, head = remove_tail(head, ListNode(0))
#
#         return head


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or (head and not head.next):
            return

        tail, cur = head, head
        for _ in range(n):
            cur = cur.next

        prev = None
        while cur:
            prev = tail
            cur = cur.next
            tail = tail.next

        if prev:
            prev.next = tail.next
            return head
        else:
            return tail.next


if __name__ == "__main__":
    s = Solution()
    head = ListNode(val=1)
    cur = head
    for x in (2, 3, 4, 5):
        node = ListNode(x)
        cur.next = node
        cur = node

    s.removeNthFromEnd(head, 2)
    for x in [1, 2, 3, 5]:
        assert head.val == x, x
        head = head.next
