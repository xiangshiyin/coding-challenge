#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        saw = {}
        for idx, num in enumerate(nums):
            if target - num in saw:
                return [saw[target - num], idx]
            saw[num] = idx


# @lc code=end
