#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def helper(root, level):
            if not root:
                return
            if level > len(ans):
                ans.append(root.val)
            helper(root.right, level + 1)
            helper(root.left, level + 1)

        helper(root, 1)
        return ans


# @lc code=end
