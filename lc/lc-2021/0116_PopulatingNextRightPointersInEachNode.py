"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         '''
#         bfs traversal the list level by level
#         '''
#         from collections import deque
#         q = deque()
#         if not root:
#             return root

#         q.append(root)
#         while q:
#             n = len(q)
#             for i in range(n):
#                 node = q.popleft()
#                 # add pointer
#                 if i < n - 1:
#                     node.next = q[0]

#                 # add children
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#             # print(n, len(q), [nd.val for nd in q])

#         return root

# bfs solution as of 11/15/2021
# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         '''
#         bfs solution
#         '''
#         # exception
#         if not root:
#             return root

#         from collections import deque
#         q = deque()
#         level = 0
#         q.append((root,level))
#         while q:
#             first, level = q.popleft()
#             if first.left:
#                 q.append((first.left, level+1))
#             if first.right:
#                 q.append((first.right, level+1))

#             while q and q[0][1] == level:
#                 new, _ = q.popleft()
#                 first.next = new
#                 first = new
#                 if first.left:
#                     q.append((first.left, level+1))
#                 if first.right:
#                     q.append((first.right, level+1))

#             first.next = None
#         return root


# better solution with no extra space usage, as of 11/15/2021
class Solution:
    def connect(self, root: "Node") -> "Node":
        """
        no extra space, leverage parent node to collect subtrees of children
        """
        # exception
        if not root:
            return root

        leftmost = root
        while leftmost.left:
            node = leftmost
            while node:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                node = node.next
            leftmost = leftmost.left

        return root


# # as of 12/3/2021
# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         '''
#         attention: "perfect binary tree"
#         dfs solution, recursion
#         '''
#         if not root:
#             return root

#         if root.left:
#             root.left.next = root.right
#             if root.next:
#                 root.right.next = root.next.left

#         root.left = self.connect(root.left)
#         root.right = self.connect(root.right)

#         return root
