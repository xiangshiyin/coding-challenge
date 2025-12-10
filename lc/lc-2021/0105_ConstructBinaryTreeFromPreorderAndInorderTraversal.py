# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None

        def build(preorder, inorder):
            if len(inorder) == 0:
                return None
            root = TreeNode(preorder[0])
            pos = inorder.index(preorder[0])
            root.left = build(preorder[1 : 1 + pos], inorder[:pos])
            root.right = build(preorder[1 + pos :], inorder[1 + pos :])

            return root

        return build(preorder, inorder)
