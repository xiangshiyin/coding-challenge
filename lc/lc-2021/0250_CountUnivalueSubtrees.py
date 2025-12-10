# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:  # None
                return (0, 1)
            if not node.left and not node.right:  # leaf node
                return (1, 1)

            l = dfs(node.left)
            r = dfs(node.right)

            if (
                l[0] * r[0] > 0
                and node.val == node.left.val
                and node.val == node.right.val
            ):
                if l[1] * r[1]:
                    return (l[0] + r[0] + 1, 1)
                else:
                    return (l[0] + r[0], 0)
            elif l[0] * r[0] > 0:
                return (l[0] + r[0], 0)
            elif not r[0]:  # empty right
                if node.val == node.left.val and l[1]:
                    return (l[0] + 1, 1)
                else:
                    return (l[0], 0)
            else:
                if node.val == node.right.val and r[1]:
                    return (r[0] + 1, 1)
                else:
                    return (r[0], 0)

        return dfs(root)[0]
