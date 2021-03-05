# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        if root:
            # left
            if root.left:
                res += self.inorderTraversal(root.left)
            # node
            res.append(root.val)

            # right
            if root.right:
                res += self.inorderTraversal(root.right)
                
        
        
        return res
        
        