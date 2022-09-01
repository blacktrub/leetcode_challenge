"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"Node: {self.val} {self.next.val if self.next else None}"


def reverse(head, next):
    real_next = head.next
    head.next = next
    if not real_next:
        return head
    return reverse(real_next, head)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        return reverse(head, None)


def head_to_list_values(head):
    out = []
    cur = head
    while True:
        out.append(cur.val)

        if not cur.next:
            return out

        cur = cur.next


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    cur = head
    for x in [2, 3, 4, 5]:
        node = ListNode(x)
        cur.next = node
        cur = node

    assert head_to_list_values(s.reverseList(head)) == [5, 4, 3, 2, 1]
