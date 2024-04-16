# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        from collections import deque
        q = deque()
        q.append(root)
        
        while q:
            n = len(q)
            res = 0
            for i in range(n):
                node = q.popleft()
                res += node.val
                # add children
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
        