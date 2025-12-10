# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         '''
#         long, iterative solution
#         '''
#         if not root.left and not root.right:
#             return True
#         elif not root.left or not root.right:
#             return False

#         # BFS search left and right, compare the results
#         from collections import deque
#         q1 = deque()
#         q2 = deque()
#         q1.append(root.left)
#         q2.append(root.right)
#         while q1 and q2:
#             n1 = q1.popleft()
#             n2 = q2.popleft()
#             if n1.val != n2.val or len(q1)!=len(q2):
#                 return False
#             # add children
#             if n1.right:
#                 q1.append(n1.right)
#             elif n1.val != 200:
#                 q1.append(TreeNode(200))

#             if n1.left:
#                 q1.append(n1.left)
#             elif n1.val != 200:
#                 q1.append(TreeNode(200))

#             if n2.left:
#                 q2.append(n2.left)
#             elif n2.val != 200:
#                 q2.append(TreeNode(200))

#             if n2.right:
#                 q2.append(n2.right)
#             elif n2.val != 200:
#                 q2.append(TreeNode(200))
#         if len(q1) != len(q2):
#             return False

#         return True

# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         '''
#         recursive solution
#         '''
#         def mirror(n1, n2):
#             if not n1 and not n2:
#                 return True
#             if not n1 or not n2:
#                 return False
#             return (n1.val == n2.val) & mirror(n1.right, n2.left) & mirror(n1.left, n2.right)

#         return mirror(root, root)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        another iterative solution
        """
        from collections import deque

        q = deque()
        q.append(root)
        q.append(root)

        while q:
            n1 = q.popleft()
            n2 = q.popleft()
            if not n1 and not n2:
                continue
            if not n1 or not n2:
                return False
            if n1.val != n2.val:
                return False
            q.append(n1.left)
            q.append(n2.right)
            q.append(n1.right)
            q.append(n2.left)
        return True
