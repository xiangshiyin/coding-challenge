#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def postorder(root):
            if not root:
                return 0, True
            dl, l = postorder(root.left)
            dr, r = postorder(root.right)
            return max(dl, dr) + 1, l and r and abs(dl - dr) <= 1

        _, ans = postorder(root)
        return ans


# @lc code=end
