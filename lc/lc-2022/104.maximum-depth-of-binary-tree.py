#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, level, depth):
            depth = level
            if node.left:
                depth = max(dfs(node.left, level + 1, depth), depth)
            if node.right:
                depth = max(dfs(node.right, level + 1, depth), depth)
            return depth

        if not root:
            return 0
        else:
            return dfs(root, 1, 1)


# @lc code=end
