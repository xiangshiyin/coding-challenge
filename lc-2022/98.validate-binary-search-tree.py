#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bottom_up(root):
            if root and not root.left and not root.right:
                return True, root.val, root.val

            min_c = root.val
            max_c = root.val
            passed = True

            if root.left:
                flg_l, min_l, max_l = bottom_up(root.left)
                if not flg_l:
                    passed = False
                elif max_l >= min_c:
                    passed = False
                else:
                    passed = True
                    min_c = min(min_c, min_l)

            if root.right:
                flg_r, min_r, max_r = bottom_up(root.right)
                if not flg_r:
                    passed = False
                elif min_r <= max_c:
                    passed = False
                else:
                    passed = passed and flg_r
                    max_c = max(max_c, max_r)
            return passed, min_c, max_c

        return bottom_up(root)[0]


# @lc code=end

