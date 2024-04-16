#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if root:
            # current root
            output += [root.val]
            # left
            if root.left:
                output += self.preorderTraversal(root.left)
            # right
            if root.right:
                output += self.preorderTraversal(root.right)
        return output


# @lc code=end

