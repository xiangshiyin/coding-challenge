#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start
# class Solution:
#     def increasingTriplet(self, nums: List[int]) -> bool:
#         """
#         O(n) in space
#         1st pass, find mins on the left
#         2nd pass, find maxs on the right
#         """
#         n = len(nums)
#         mins = [nums[0] for i in range(n)]
#         maxs = nums[-1]
#         # 1st pass
#         for i in range(1, n):
#             mins[i] = min(mins[i - 1], nums[i - 1])
#         # 2nd pass
#         for i in range(n - 2, 0, -1):
#             maxs = max(maxs, nums[i + 1])
#             if nums[i] < maxs and nums[i] > mins[i]:
#                 return True
#         return False

# solution on 2022-09-25
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        O(1) in space
        """
        import math

        first = second = math.inf
        for num in nums:
            if num < first:
                first = num
            elif num < second and num > first:
                second = num
            if second < num:
                return True
        return False


# @lc code=end
