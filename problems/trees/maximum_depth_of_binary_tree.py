"""
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
    The number of nodes in the tree is in the range [0, 104].
    -100 <= Node.val <= 100
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root, n):
    if not root:
        return n

    max1 = max_depth(root.left, n + 1)
    max2 = max_depth(root.right, n + 1)
    return max(max1, max2)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return max_depth(root, 0)
