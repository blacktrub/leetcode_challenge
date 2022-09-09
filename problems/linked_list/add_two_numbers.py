from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode()
        additional = 0
        cur = head
        while l1 or l2:
            s = additional
            if l1:
                s += l1.val
            if l2:
                s += l2.val

            additional = 0

            if s > 9:
                s = s - 10
                additional = 1

            cur.val = s
            if (l1 and l1.next) or (l2 and l2.next):
                cur.next = ListNode()
                cur = cur.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        if additional:
            node = ListNode(additional)
            cur.next = node

        return head


if __name__ == "__main__":
    s = Solution()
    head1 = ListNode(val=2)
    cur = head1
    for x in (4, 3):
        node = ListNode(x)
        cur.next = node
        cur = node

    head2 = ListNode(val=5)
    cur = head2
    for x in (6, 4):
        node = ListNode(x)
        cur.next = node
        cur = node

    ans = s.addTwoNumbers(head1, head2)
    for x in (7, 0, 8):
        print(x, ans.val)
        assert ans.val == x
        ans = ans.next
