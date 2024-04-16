#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.ans = ""

        def preorder(root):
            if not root:
                self.ans += "#,"
                return
            self.ans += f"{root.val},"
            preorder(root.left)
            preorder(root.right)

        preorder(root)

        return self.ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        from collections import deque

        nodes = deque(data.rstrip(",").split(","))

        def build(nodes):
            if not nodes:
                return None
            first = nodes.popleft()
            if first == "#":
                return None
            root = TreeNode(int(first))
            root.left = build(nodes)
            root.right = build(nodes)
            return root

        return build(nodes)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
