#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l = i = 0
        r = n - 1
        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1  # must be 1, so no need to check again
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1  # could be 0 or 1, so need to check i again in next iteration
            else:
                i += 1

        return nums


# @lc code=end

