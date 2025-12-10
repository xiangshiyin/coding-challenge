# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        freq = {}
        output = []

        def postorder(node):
            res = ""
            if node:
                res = f"{postorder(node.left)},{postorder(node.right)},{node.val}"
            # update the hash table
            if res not in freq:
                freq[res] = 1
            else:
                freq[res] += 1
                if freq[res] == 2 and res != "":
                    output.append(node)

            return res

        postorder(root)

        return output
