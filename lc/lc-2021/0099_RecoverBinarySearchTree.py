# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def recoverTree(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         #### O(n) solution via print out the list
#         def dfs(node):
#             res = []
#             if node.left:
#                 res += dfs(node.left)
#             res.append(node)
#             if node.right:
#                 res += dfs(node.right)
#             return res
        
#         thelist = dfs(root)
#         # print([node.val for node in thelist])
        
#         # find the two nodes
#         ix = 0
#         while ix < len(thelist) - 1 and thelist[ix].val <= thelist[ix + 1].val:
#             ix += 1
#         l = thelist[ix]
#         jx = len(thelist) - 1
#         while jx >= 0 and thelist[jx].val >= thelist[jx - 1].val:
#             jx -= 1
#         r = thelist[jx]
        
#         # swap the two node values
#         tmp = l.val
#         l.val = r.val
#         r.val = tmp


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        '''
        iterative traversal
        '''
        stack = []
        x = y = parent = None
        while True:
            while root:
                stack.append(root)
                root = root.left
            
            if not stack:
                break
            
            node = stack.pop()
            
            if parent and node.val < parent.val:
                y = node
                if not x:
                    x = parent
                
            
            parent = node
            root = node.right
            
        x.val, y.val = y.val, x.val
        
        
        

