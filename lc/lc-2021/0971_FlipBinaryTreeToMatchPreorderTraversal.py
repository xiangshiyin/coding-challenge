# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.ix = 0
        self.flipped = []
        self.n = len(voyage)

        def preorder(node):
            if node:
                if node.val == voyage[self.ix]:
                    self.ix += 1
                    if (
                        self.ix < self.n
                        and node.left
                        and node.left.val != voyage[self.ix]
                    ):
                        self.flipped.append(node.val)
                        preorder(node.right)
                        preorder(node.left)
                    else:
                        preorder(node.left)
                        preorder(node.right)
                else:
                    self.flipped.append(-1)

        preorder(root)

        if self.flipped:
            for flg in self.flipped:
                if flg == -1:
                    self.flipped = [-1]
                    break

        return self.flipped
