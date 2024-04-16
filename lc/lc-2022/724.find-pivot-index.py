#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        cur_total = 0

        for i, num in enumerate(nums):
            if cur_total * 2 + num == total:
                return i
            cur_total += num

        return -1


# @lc code=end

