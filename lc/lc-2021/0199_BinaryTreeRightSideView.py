# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
        BFS traversal, iterate through nodes at the same level in each iteration
        Only record right node if there is any
        """
        if root == None:
            return None

        from collections import deque

        queue = deque([root])
        output = []

        while queue:
            # update output
            output.append(queue[0].val)

            # pop
            for i in range(len(queue)):
                node = queue.popleft()
                # append new nodes
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

        return output
