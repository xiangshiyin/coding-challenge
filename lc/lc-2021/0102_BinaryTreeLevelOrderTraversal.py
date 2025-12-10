# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        from collections import deque

        q = deque()

        if not root:
            return ans
        else:
            q.append((root, 0))
            while q:
                node, level = q.popleft()
                if len(ans) == level:
                    ans.append([node.val])
                else:
                    ans[level].append(node.val)

                # add children
                if node.left:
                    q.append((node.left, level + 1))
                if node.right:
                    q.append((node.right, level + 1))
            return ans
