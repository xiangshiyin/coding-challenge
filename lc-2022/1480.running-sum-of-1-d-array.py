#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rsum = []
        for num in nums:
            if not rsum:
                rsum.append(num)
            else:
                rsum.append(num + rsum[-1])
        return rsum

# @lc code=end

