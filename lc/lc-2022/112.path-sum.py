#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        self.output = False

        def dfs(root, path, targetSum):
            if not self.output:
                if not root.left and not root.right:
                    if path == targetSum:
                        self.output = True  # found
                else:
                    if root.left:
                        dfs(root.left, path + root.left.val, targetSum)
                    if root.right:
                        dfs(root.right, path + root.right.val, targetSum)

        dfs(root, root.val, targetSum)
        return self.output


# @lc code=end
