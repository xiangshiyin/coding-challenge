# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         '''
#         only beats 6%
#         '''
#         self.min_level = 0
#         self.ans = None
        
#         def dfs(node, level):
#             '''
#             dfs search from every node, see if p and q show up as descendants
#             '''
#             res = [False, False]
            
#             if not node:
#                 return res
            
#             if node == p:
#                 res[0] = True
#             if node == q:
#                 res[1] = True
                
#             # check the children
#             lres = dfs(node.left, level + 1)
#             rres = dfs(node.right, level + 1)
                
#             res[0] = res[0] | lres[0] | rres[0]
#             res[1] = res[1] | lres[1] | rres[1]
            
#             if res[0] and res[1] and level >= self.min_level:
#                 self.min_level = level
#                 self.ans = node
            
#             return res
        
#         dfs(root, 0)
        
#         return self.ans

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        utilize the property of binary search tree
        '''
        
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
            
                
                
    
    