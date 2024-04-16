#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = {0: 1}
        curr = 0
        counter = 0
        for num in nums:
            curr += num
            if curr - k in presum:
                counter += presum[curr - k]
            if curr not in presum:
                presum[curr] = 1
            else:
                presum[curr] += 1
        return counter


# @lc code=end
