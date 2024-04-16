"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

# class Solution: # the hashset solution
#     def findRoot(self, tree: List['Node']) -> 'Node':
#         # exception
#         if len(tree)==1:
#             return tree[0]
#         # 1st pass, traverse the list
#         seen = set() # the hashset
#         for node in tree:
#             seen.update(node.children)
#         # 2nd pass, find the root
#         for node in tree:
#             if node not in seen:
#                 return node

class Solution: # the YOLO solution
    def findRoot(self, tree: List['Node']) -> 'Node':
        valueSum = 0
        # 1st pass
        for node in tree:
            valueSum += node.val
            valueSum -= sum([c.val for c in node.children])
            
        # 2nd pass
        for node in tree:
            if node.val==valueSum:
                return node
            