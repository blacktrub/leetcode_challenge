class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        p_path = q_path = 0
        cur = p
        while cur != root:
            p_path += 1

        cur = q
        while cur != root:
            q_path += 1

        while True:
            if p == q:
                return p

            if p_path > q_path:
                p = p.p
