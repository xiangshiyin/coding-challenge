#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []

        def helper(node, currPath, currSum, targetSum):
            if not node:
                return
            currSum += node.val
            if not node.left and not node.right and currSum == targetSum:
                ans.append(currPath + [node.val])
            else:
                helper(node.left, currPath + [node.val], currSum, targetSum)
                helper(node.right, currPath + [node.val], currSum, targetSum)

        helper(root, [], 0, targetSum)

        return ans


# @lc code=end
