"""
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:
    The number of nodes in the list is in the range [1, 5 * 104].
    1 <= Node.val <= 1000
"""


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)


def reverse_list(head, next):
    if not head:
        return head
    old_next = head.next
    head.next = next
    if not old_next:
        return head
    return reverse_list(old_next, head)


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or head and not head.next:
            return head

        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        slow_next = slow.next
        slow.next = None
        reversed_second_part = reverse_list(slow_next, None)

        cur = head
        while cur and reversed_second_part:
            old_next = cur.next
            old_reversed = reversed_second_part.next
            cur.next = reversed_second_part
            reversed_second_part.next = old_next

            reversed_second_part = old_reversed
            cur = old_next


if __name__ == "__main__":
    s = Solution()
    head = ListNode(val=1)
    cur = head
    for x in (2, 3, 4, 5):
        node = ListNode(x)
        cur.next = node
        cur = node

    s.reorderList(head)
    for x in [1, 5, 2, 4, 3]:
        assert head.val == x, x
        head = head.next

    head = ListNode(val=1)
    s.reorderList(head)
