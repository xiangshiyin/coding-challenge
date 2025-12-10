# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     '''
#     recursive solution
#     '''
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         if root:
#             if root.left:
#                 res += self.inorderTraversal(root.left)
#             res.append(root.val)
#             if root.right:
#                 res += self.inorderTraversal(root.right)

#         return res


class Solution:
    """
    iterative solution
    """

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
