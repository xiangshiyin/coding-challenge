# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def postorderTraversal(self, root: TreeNode) -> List[int]:
#         '''
#         recursion solution
#         '''
#         res = []
#         if root:
#             if root.left:
#                 res += self.postorderTraversal(root.left)
#             if root.right:
#                 res += self.postorderTraversal(root.right)
#             res.append(root.val)
#         return res

# class Solution:
#     def postorderTraversal(self, root: TreeNode) -> List[int]:
#         '''
#         iterative solution, preorder reversed
#         '''
#         res = []
#         stack = []
        
#         if root:
#             stack.append(root)
#         while stack:
#             node = stack.pop()
#             res.append(node.val)
#             if node.left:
#                 stack.append(node.left)
#             if node.right:
#                 stack.append(node.right)
#         return res[::-1]

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        iterative solution
        '''
        res = []
        if root:
            stack = [(root, False)]
            while stack:
                node, visited = stack.pop()
                if visited:
                    res.append(node.val)
                else:
                    stack.append((node, True))
                    if node.right:
                        stack.append((node.right, False))
                    if node.left:
                        stack.append((node.left, False))
        
        return res
    
        

