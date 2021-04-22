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
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         if root:
#             res.append(root.val)
#             if root.left:
#                 res += self.preorderTraversal(root.left)
#             if root.right:
#                 res += self.preorderTraversal(root.right)
#         return res
            
            
class Solution:
    '''
    iterative solution
    '''
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
    
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
            