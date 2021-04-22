# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        dfs, bottom up
        '''
        self.ans = None
        
        def dfs(node, p, q):
            if not node:
                return 0
            
            lres = dfs(node.left, p, q) if node.left else 0
            rres = dfs(node.right, p, q) if node.right else 0
            nres = 1 if node == p else 2 if node == q else 0
            
            if lres + rres + nres == 3:
                self.ans = node
                return 0
            
            return max(lres, rres, nres)
        
        dfs(root, p, q)
        
        return self.ans
    