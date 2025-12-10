# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int: # recursion
#         self.ans = 0

#         def dfs(node, level):
#             if not node:
#                 return
#             elif not node.left and not node.right: # leaf node
#                 self.ans = max(self.ans, level)
#             else:
#                 dfs(node.left, level+1)
#                 dfs(node.right, level+1)

#         if root:
#             dfs(root, 1)

#         return self.ans


class Solution(object):
    def maxDepth(self, root):
        """
        BFS solution
        """
        depth = 0
        if root:
            level = [root]
            while level:
                depth += 1
                q = []
                for l in level:
                    if l.left:
                        q.append(l.left)
                    if l.right:
                        q.append(l.right)
                level = q

        return depth
