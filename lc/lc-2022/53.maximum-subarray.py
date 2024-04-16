#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = - 10 ** 4 - 1
        cur_sum = 0
        for num in nums:
            if cur_sum < 0 and cur_sum < num:
                cur_sum = num
            else:
                cur_sum += num
            max_sum = max(max_sum, cur_sum)
        return max_sum


        
# @lc code=end

