# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        with stack
        '''
        # exceptions
        if not root1:
            return root2
        if not root2:
            return root1
        
        stack = []
        stack.append([root1, root2])
        while stack:
            l, r = stack.pop()
            # update l node val
            l.val += r.val
            # append children
            if l.left and r.left:
                stack.append([l.left, r.left])
            elif not l.left:
                l.left = r.left
            
            if l.right and r.right:
                stack.append([l.right, r.right])
            elif not l.right:
                l.right = r.right

        return root1

# as of 11/15/2021, recursion, preorder traversal
# class Solution:
#     def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
#         '''
#         pre-order traversal
#         '''
#         if not root1:
#             return root2
#         if not root2:
#             return root1
        
#         root1.val += root2.val
#         root1.left = self.mergeTrees(root1.left, root2.left)
#         root1.right = self.mergeTrees(root1.right, root2.right)
        
#         return root1
    
    
# as of 12/2/2021
# class Solution:
#     def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
#         if not root1:
#             return root2
#         if not root2:
#             return root1
        
#         root = TreeNode(val=root1.val+root2.val)
#         root.left = self.mergeTrees(root1.left, root2.left)
#         root.right = self.mergeTrees(root1.right, root2.right)
        
#         return root
    
    
