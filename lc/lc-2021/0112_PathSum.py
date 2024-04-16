# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        '''
        dfs solution
        '''
        def dfs(node, cur):
            if not node.left and not node.right: # leaf node
                if cur == targetSum:
                    return True
                else:
                    return False
                
            l = dfs(node.left, cur + node.left.val) if node.left else False
            r = dfs(node.right, cur + node.right.val) if node.right else False
            return l | r
        return dfs(root, root.val) if root else False
    
                

                