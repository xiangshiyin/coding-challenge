#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def root_left_right(root):
            output = []
            if root:
                output += [root.val]
                if root.left:
                    output += root_left_right(root.left)
                else:
                    output += [None]
                if root.right:
                    output += root_left_right(root.right)
                else:
                    output += [None]

            return output

        def root_right_left(root):
            output = []
            if root:
                output += [root.val]
                if root.right:
                    output += root_right_left(root.right)
                else:
                    output += [None]
                if root.left:
                    output += root_right_left(root.left)
                else:
                    output += [None]
            return output

        if not root.left:
            if root.right:
                return False
            else:
                return True
        else:
            if not root.right:
                return False
            else:
                return root_left_right(root.left) == root_right_left(root.right)


# @lc code=end
