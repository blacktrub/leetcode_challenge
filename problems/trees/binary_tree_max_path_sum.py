"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

Constraints:
    The number of nodes in the tree is in the range [1, 3 * 104].
    -1000 <= Node.val <= 1000
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(root):
            if not root:
                return 0

            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)
            nonlocal res
            res = max(res, root.val + left + right)
            return root.val + max(left, right)

        dfs(root)
        return res


# class Solution:
#     def maxPathSum(self, root: Optional[TreeNode]) -> int:
#         cache = {}
#
#         def max_path(root):
#             if not root:
#                 return float("-infinity")
#
#             left, right = max_path(root.left), max_path(root.right)
#             cache[id(root)] = max(
#                 root.val + (left if left > 0 else 0) + (right if right > 0 else 0),
#                 left,
#                 right,
#                 root.val,
#             )
#
#             return max(
#                 root.val + right,
#                 root.val + left,
#                 root.val,
#             )
#
#         def max_sum(root):
#             if not root:
#                 return float("-infinity")
#
#             if id(root) in cache:
#                 s = cache[id(root)]
#             else:
#                 s = root.val
#                 s += max(max_path(root.left), 0)
#                 s += max(max_path(root.right), 0)
#
#             return max(s, max_sum(root.left) or s, max_sum(root.right) or s)
#
#         return max_sum(root)


if __name__ == "__main__":
    assert Solution().maxPathSum(TreeNode(1, TreeNode(2), TreeNode(3))) == 6
    assert Solution().maxPathSum(TreeNode(1, TreeNode(-2), TreeNode(3))) == 4
    assert Solution().maxPathSum(TreeNode(-2, TreeNode(-1))) == -1
