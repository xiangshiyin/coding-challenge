#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#         n = len(nums)

#         def helper(left, right):
#             if left > right:
#                 return
#             mid = (left + right) // 2
#             root = TreeNode(val=nums[mid])
#             root.left = helper(left, mid - 1)
#             root.right = helper(mid + 1, right)
#             return root

#         return helper(0, n - 1)


# solution on 2022-10-25
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        r = len(nums) - 1
        m = r // 2
        root = TreeNode(val=nums[m])
        if m > 0:
            root.left = self.sortedArrayToBST(nums[:m])
        if m + 1 < len(nums):
            root.right = self.sortedArrayToBST(nums[m + 1 :])
        return root


# @lc code=end
