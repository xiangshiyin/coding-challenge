#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         output = []
#         if not root:
#             return []
#         else:
#             output.append(root.val)
#             for child in root.children:
#                 output.extend(self.preorder(child))
#             return output


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        output = []
        if not root:
            return output
        else:
            output.append(root.val)
            for c in root.children:
                output += self.preorder(c)
            return output


# @lc code=end
