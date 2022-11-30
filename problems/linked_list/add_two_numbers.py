from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def merge(first, second, add=0):
            if not first and not second:
                return ListNode(add) if add else None

            sm = 0 + add
            sm += first.val if first else 0
            sm += second.val if second else 0

            node = ListNode(sm % 10)
            node.next = merge(
                first.next if first else None,
                second.next if second else None,
                sm // 10,
            )
            return node

        return merge(l1, l2)


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
        assert ans.val == x
        ans = ans.next
