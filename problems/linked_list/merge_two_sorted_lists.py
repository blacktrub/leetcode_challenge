"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        out = f"Node: {self.val} "
        cur = self.next
        while cur:
            out += f"-> Node({cur.val}) "
            cur = cur.next
        return out


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode()
        tail = head
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return head.next


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
    for x in [2, 4]:
        node = ListNode(x)
        cur.next = node
        cur = node

    head2 = ListNode(1)
    cur = head2
    for x in [3, 4]:
        node = ListNode(x)
        cur.next = node
        cur = node

    assert head_to_list_values(s.mergeTwoLists(head, head2)) == [1, 1, 2, 3, 4, 4]
