#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
#         output = []

#         def dfs(root, path, output):
#             if not root.left and not root.right:
#                 output.append("->".join([str(node.val) for node in path]))
#             if root.left:
#                 dfs(root.left, path + [root.left], output)
#             if root.right:
#                 dfs(root.right, path + [root.right], output)

#         dfs(root, [root], output)
#         return output


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        output = []

        def dfs(root, path):
            if not root.left and not root.right:
                output.append(path)
            if root.left:
                dfs(root.left, f"{path}->{root.left.val}")
            if root.right:
                dfs(root.right, f"{path}->{root.right.val}")

        dfs(root, f"{root.val}")
        return output


# @lc code=end
