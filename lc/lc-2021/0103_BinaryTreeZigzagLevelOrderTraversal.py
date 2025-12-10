# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        bfs traversal, switch left/right order based on level
        """

        ans = []

        # special case
        if not root:
            return ans

        from collections import deque

        q = deque()
        q.append(root)
        level = 0  # 0 represents the level of the tree node

        while q:
            n = len(q)
            tmp = []
            for i in range(n):
                node = q.popleft()
                tmp.append(node.val)
                # add children:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not level % 2:
                ans.append(tmp)
            else:
                ans.append(tmp[::-1])
            level += 1

        return ans
