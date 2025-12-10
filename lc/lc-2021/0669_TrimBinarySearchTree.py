# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        """
        function runs faster with less parameters
        """

        def trim(node):
            if node:
                if node.val > high:  # need to remove right subtree
                    return trim(node.left)
                elif node.val < low:  # need to remove left subtree
                    return trim(node.right)
                else:  # in range
                    node.left = trim(node.left)
                    node.right = trim(node.right)
                    return node
            else:
                return None

        return trim(root)
