# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    inorder traversal
    """

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.prev = 0

        def traverse(node):
            if node:
                traverse(node.right)
                node.val += self.prev
                self.prev = node.val
                traverse(node.left)

        traverse(root)
        return root
