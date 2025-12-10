# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        """
        BFS traversal to level d - 1, add new nodes
        """
        # exception
        if d == 1:
            nhead = TreeNode(val=v, left=root)
            return nhead

        from collections import deque

        q = deque()
        q.append(root)
        level = 1

        # get the list of parent nodes
        while level < d - 1:
            n = len(q)
            for i in range(n):
                node = q.popleft()  # tp represents l or r
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        # iterate through the parent nodes, and a new row
        for node in q:
            lnode = TreeNode(val=v, left=node.left)
            rnode = TreeNode(val=v, right=node.right)
            node.left = lnode
            node.right = rnode

        return root
