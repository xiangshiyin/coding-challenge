#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        max(max(depth_left + depth_right))
        """
        self.ans = 0

        def postorder(root):
            if not root:
                return 0
            dl = postorder(root.left)
            dr = postorder(root.right)
            self.ans = max(self.ans, dl + dr)
            return max(dl, dr) + 1

        postorder(root)
        return self.ans


# @lc code=end
