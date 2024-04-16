#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()

        def help(root, k):
            if not root:
                return False
            if k - root.val in seen:
                return True
            seen.add(root.val)
            return help(root.left, k) or help(root.right, k)

        return help(root, k)


# @lc code=end

