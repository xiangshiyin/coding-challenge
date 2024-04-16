#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         output = []
#         # exception
#         if not root:
#             return output

#         from collections import deque
#         q = deque()
#         level = 0
#         q.append([root, level])
#         while q:
#             cur = []
#             while q and q[0][1] == level:
#                 node, _ = q.popleft() # pop
#                 cur.append(node.val)
#                 if node.left:
#                     q.append([node.left, level + 1])
#                 if node.right:
#                     q.append([node.right, level + 1])
#             level += 1
#             output.append(cur)

#         return output

# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []

#         from collections import deque

#         q = deque()
#         q.append([root, 0])
#         output = []
#         while q:
#             node, level = q.popleft()
#             if len(output) == level:
#                 output.append([node.val])
#             else:
#                 output[-1].append(node.val)

#             if node.left:
#                 q.append([node.left, level + 1])
#             if node.right:
#                 q.append([node.right, level + 1])

#         return output


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque

        output = []
        q = deque([(root, 0)])

        while q:
            node, level = q.popleft()
            if not node:
                break
            if not output or level + 1 > len(output):
                output.append([node.val])
            else:
                output[-1].append(node.val)
            # add children
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        return output


# @lc code=end

