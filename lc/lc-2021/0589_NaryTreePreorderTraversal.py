"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        s = []
        ans = []

        if not root:
            return ans

        s.append(root)
        while s:
            node = s.pop()
            ans.append(node.val)
            for c in node.children[::-1]:
                s.append(c)
        return ans
