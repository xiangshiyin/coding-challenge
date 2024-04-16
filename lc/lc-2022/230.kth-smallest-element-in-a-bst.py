#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         self.rank = 0
#         self.ans = None

#         def inorder(root, k):
#             if root.left:
#                 inorder(root.left, k)
#             self.rank += 1
#             if self.rank == k:
#                 self.ans = root.val
#                 return
#             if root.right:
#                 inorder(root.right, k)

#         inorder(root, k)
#         return self.ans


# solution on 2022-10-04
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         self.rank = 0
#         self.ans = None

#         def inorder(root, k):
#             if root.left:
#                 inorder(root.left, k)
#             self.rank += 1
#             if self.rank == k:
#                 self.ans = root.val
#                 return
#             if root.right:
#                 inorder(root.right, k)

#         inorder(root, k)
#         return self.ans


# solution on 2022-10-25
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.rank = 0
        self.ans = None

        def inorder(root, k):
            if root.left:
                inorder(root.left, k)

            self.rank += 1
            if self.rank == k:
                self.ans = root.val
                return

            if root.right:
                inorder(root.right, k)

        inorder(root, k)
        return self.ans


# @lc code=end
