from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if not root.right and not root.left:
            return True

        if not root.right or not root.left:
            return False

        q = deque([root.left, root.right])
        while q:
            n1: TreeNode = q.popleft()
            n2: TreeNode = q.popleft()

            if n1.val != n2.val:
                return False

            if n1.right and n2.left:
                if n1.right.val != n2.left.val:
                    return False
                q.append(n1.right)
                q.append(n2.left)
            elif n1.right:
                return False
            elif n2.left:
                return False

            if n2.right and n1.left:
                if n2.right.val != n1.left.val:
                    return False
                q.append(n2.right)
                q.append(n1.left)
            elif n2.right:
                return False
            elif n1.left:
                return False

        return True
