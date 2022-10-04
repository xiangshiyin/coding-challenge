#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(preorder, inorder):
            if len(preorder) == 0 or len(inorder) == 0:
                return None
            v = preorder[0]
            root = TreeNode(val=v)
            cutoff = inorder.index(v)
            root.left = helper(preorder[1 : cutoff + 1], inorder[:cutoff])
            root.right = helper(preorder[cutoff + 1 :], inorder[cutoff + 1 :])

            return root

        return helper(preorder, inorder)


# @lc code=end
