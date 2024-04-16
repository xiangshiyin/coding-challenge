#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# class Solution:
#     def lowestCommonAncestor(
#         self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
#     ) -> "TreeNode":
#         # find p
#         path_p = set()
#         node = root
#         while node and node != p:
#             path_p.add(node)
#             if node.val > p.val:
#                 node = node.left
#             else:
#                 node = node.right
#         path_p.add(node)

#         # find q
#         node = root
#         output = None
#         while node != q:
#             if node in path_p:
#                 output = node
#                 print(output.val)
#             if node.val > q.val:
#                 node = node.left
#             else:
#                 node = node.right
#         if node in path_p:
#             output = q
#         return output


# class Solution:
#     def lowestCommonAncestor(
#         self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
#     ) -> "TreeNode":
#         while root:
#             if root.val > p.val and root.val > q.val:
#                 root = root.left
#             elif root.val < p.val and root.val < q.val:
#                 root = root.right
#             else:
#                 return root

# solution on 2022-09-15
class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        while root:
            if root and root.val > p.val and root.val > q.val:
                root = root.left
            elif root and root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root


# @lc code=end

