"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 104].
    -1000 <= Node.val <= 1000
"""

from collections import deque
import json


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        [root, left, right, left_left, left_right, right_left, right_right]
        """
        if not root:
            return ""

        q = deque([root])
        res = [root.val]
        while q:
            n = q.popleft()
            left = n.left.val if n.left else None
            right = n.right.val if n.right else None
            res += [left, right]
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

        while res[-1] is None:
            res.pop()

        return json.dumps(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        [root, left, right, left_left, left_right, right_left, right_right]
        """

        if not data:
            return

        nodes = json.loads(data)
        if not nodes:
            return

        head = TreeNode(int(nodes[0]))
        q = deque([head])
        i = 1
        while q and i < len(nodes):
            n = q.popleft()
            left = TreeNode(int(nodes[i])) if nodes[i] is not None else None
            right = (
                TreeNode(int(nodes[i + 1]))
                if i + 1 < len(nodes) and nodes[i + 1] is not None
                else None
            )
            n.left = left
            n.right = right
            if left:
                q.append(left)
            if right:
                q.append(right)

            i += 2
        return head


def print_tree(r):
    q = deque([r])
    while q:
        n = q.popleft()
        print(n.val if n else None)
        if n:
            q.append(n.left)
            q.append(n.right)


if __name__ == "__main__":
    codec = Codec()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(5)
    print(codec.serialize(root))
