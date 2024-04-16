#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if root:
            if root.left:
                output += self.inorderTraversal(root.left)
            output += [root.val]
            if root.right:
                output += self.inorderTraversal(root.right)
        return output


# @lc code=end

