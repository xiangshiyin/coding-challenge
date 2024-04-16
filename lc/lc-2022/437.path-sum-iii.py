#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        trick: presum
        """
        if not root:
            return 0

        from collections import defaultdict

        self.prePathSum = defaultdict(int)
        self.prePathSum[0] = 1
        self.ans = 0

        def preorder(root, target, currPathSum):
            if not root:
                return

            newPathSum = currPathSum + root.val
            self.ans += self.prePathSum[newPathSum - target]
            # update the lookup table
            self.prePathSum[newPathSum] += 1
            # visit the children
            preorder(root.left, target, newPathSum)
            preorder(root.right, target, newPathSum)
            # reset the lookup table
            self.prePathSum[newPathSum] -= 1

        preorder(root, targetSum, 0)
        return self.ans


# @lc code=end
