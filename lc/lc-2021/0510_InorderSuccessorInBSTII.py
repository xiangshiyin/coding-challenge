"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

# class Solution:
#     def inorderSuccessor(self, node: 'Node') -> 'Node':
#         '''
#         two steps:
#         1. check if right child exists, and then find the left most node in the right child
#         2. if no right child, check parent. if current node is parent's left child, return parent. if current node is parent's right child,
#         check parent's parent
#         '''

#         def check_child(node):
#             if not node.right:
#                 return None
#             else:
#                 node = node.right
#                 while node.left:
#                     node = node.left
#                 return node

#         def check_parent(node):
#             if not node.parent:
#                 return None
#             else:
#                 if node.parent.left == node:
#                     return node.parent
#                 else:
#                     return check_parent(node.parent)

#         found_child = check_child(node)
#         if found_child:
#             return found_child
#         else:
#             return check_parent(node)


class Solution:
    def inorderSuccessor(self, node: "Node") -> "Node":
        target = node
        if not node:
            return None

        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        else:
            if not node.parent:
                return None
            else:
                if node.parent.left == node:
                    return node.parent
                else:
                    while node and node.val <= target.val:
                        node = node.parent

                    return node
