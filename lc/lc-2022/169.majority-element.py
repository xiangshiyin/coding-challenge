#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        ans = None
        for num in nums:
            if counter == 0:
                ans = num
                counter += 1
            elif num == ans:
                counter += 1
            else:
                counter -= 1

        return ans


# @lc code=end
