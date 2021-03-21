# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def averageOfLevels(self, root: TreeNode) -> List[float]:
#         '''
#         bfs
#         '''
#         from collections import deque
#         q = deque([root])
#         ans = []
        
#         while q:
#             n = len(q)
#             cumsum = 0
#             # pop out all nodes of the same level, add childrens
#             for i in range(n):
#                 node = q.popleft()
#                 cumsum += node.val
#                 # append children
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#             ans.append(cumsum / n)
#         return ans


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        '''
        dfs
        '''
        cumsum = []
        count = []
        
        def dfs(node, level):
            if len(cumsum) == level:
                cumsum.append(node.val)
                count.append(1)
            else:
                cumsum[level] += node.val
                count[level] += 1
            
            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)
        
        dfs(root, 0)
            
        return [total / n for total, n in zip(cumsum, count)]
        
        
        
        
        
        
        
        
        
        