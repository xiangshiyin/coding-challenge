# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def bottomup(node):
            v_max = 1 << 31
            v_min = -1 * 1 << 31 - 1

            if not node.left and not node.right:
                return (
                    True,
                    node.val,
                    node.val,
                )  # validity, min of subtree, max of subtree

            lres = bottomup(node.left) if node.left else (True, v_max, v_min)
            rres = bottomup(node.right) if node.right else (True, v_max, v_min)

            if node.left and node.right:
                ans = node.val > lres[2] and node.val < rres[1] and lres[0] and rres[0]
            elif node.left:
                ans = node.val > lres[2] and lres[0]
            else:
                ans = node.val < rres[1] and rres[0]

            return ans, min(lres[1], rres[1], node.val), max(lres[2], rres[2], node.val)

        return bottomup(root)[0]
