#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
#         if not root:
#             return None
#         if root.val == key:
#             tmp = root.left
#             root = root.right
#             if root and tmp:
#                 node = root
#                 while node and node.left:
#                     node = node.left
#                 node.left = tmp
#             elif not tmp:
#                 return root
#             else:
#                 return tmp

#         if root.val > key:
#             root.left = self.deleteNode(root.left, key)
#         if root.val < key:
#             root.right = self.deleteNode(root.right, key)
#         return root


# solution on 2022-10-03
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        if root.val == key:
            left = root.left
            root = root.right
            if root and left:
                node = root
                while node and node.left:
                    node = node.left
                node.left = left
            elif not left:
                return root
            else:
                return left

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root


# @lc code=end
