# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        dfs from root, pass along the max value found on the way
        """
        self.ans = 0

        def dfs(node, curmax):
            if not node:
                return
            if node.val >= curmax:
                # print(node.val)
                self.ans += 1
                curmax = node.val

            # check the children
            if node.left:
                dfs(node.left, curmax)
            if node.right:
                dfs(node.right, curmax)

        if not root:
            return self.ans
        else:
            dfs(root, root.val)
            return self.ans
