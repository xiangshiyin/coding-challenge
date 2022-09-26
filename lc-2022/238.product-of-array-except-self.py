#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1 for i in range(n)]
        rprod = 1
        # 1st pass, find product to the left
        for i in range(1, n):
            output[i] = output[i - 1] * nums[i - 1]
        # 2nd pass, find the product to the right
        for i in range(n - 2, -1, -1):
            rprod = rprod * nums[i + 1]
            output[i] = output[i] * rprod

        return output


# @lc code=end
