"""
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    m = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diam(root):
            if not root:
                return -1

            left = diam(root.left)
            right = diam(root.right)
            self.m = max(self.m, 2 + left + right)
            return 1 + max(left, right)

        diam(root)
        return self.m


# TreeNode(val: 6, left: TreeNode(val: 4, left: TreeNode(val: 2, left: None, right: None), right: TreeNode(val: 2, left: None, right: None)), right: TreeNode(val: 2, left: None, right: None))
