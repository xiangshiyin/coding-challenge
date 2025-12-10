#
# @lc app=leetcode id=1038 lang=python3
#
# [1038] Binary Search Tree to Greater Sum Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        """same as LC-538"""
        self.total = 0

        def inorder(root):
            if root:
                if root.right:
                    inorder(root.right)
                self.total += root.val
                root.val = self.total
                if root.left:
                    inorder(root.left)

        inorder(root)
        return root


# @lc code=end
