# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        '''
        in-order traversal
        '''
        self.found = False
        def inorder(node, target):
            if not node:
                return
            
            if node.left:
                l = inorder(node.left, target)
                if l:
                    return l
                
            if self.found:
                return node
            elif node == target:
                self.found = True
            
            
            if node.right:
                r = inorder(node.right, target)
                if r:
                    return r
            
            return 
    
        res = inorder(root, p)
        return res
        
## 4/8/2021: iterative solution
# class Solution:
#     def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
#         '''
#         inorder traversal the tree, find the child node of the target node
#         '''
#         curr = None
#         stack = []        
        
#         while True:
#             while root:
#                 stack.append(root)
#                 root = root.left
#             if not stack:
#                 return None
#             node = stack.pop()
#             if curr == p:
#                 return node
#             curr = node
#             root = node.right




