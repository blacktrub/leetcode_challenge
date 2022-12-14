"""
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
    a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true

Constraints:
    The number of nodes in the tree is in the range [0, 5000].
    -104 <= Node.val <= 104
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root):
    if not root:
        return 0

    left = is_balanced(root.left)
    right = is_balanced(root.right)
    return 1 + max(left, right)


def scan(root):
    if not root:
        return True

    left = is_balanced(root.left)
    right = is_balanced(root.right)
    return abs(left - right) <= 1 and scan(root.left) and scan(root.right)


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return True, 0

            lr, lh = dfs(root.left)
            rr, rh = dfs(root.right)
            balanced = lr and rr and (abs(lh - rh) <= 1)
            return balanced, 1 + max(lh, rh)

        return dfs(root)[0]
