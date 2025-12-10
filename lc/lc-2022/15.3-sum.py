#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums2, target):
        """
        nums2 is pre-sorted
        """
        l = 0
        r = len(nums2) - 1
        output = []
        seen = set()
        while l < r:
            if nums2[l] + nums2[r] + target > 0:
                r -= 1
            elif nums2[l] + nums2[r] + target < 0:
                l += 1
            else:
                if nums2[l] not in seen:
                    output.append([nums2[l], nums2[r], target])
                    seen.add(nums2[l])
                r -= 1
        return output

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums2 = sorted(nums)
        output = []
        seen = set()
        while nums2:
            target = nums2.pop()
            if target not in seen:
                output += self.twoSum(nums2, target)
                seen.add(target)
        return output


# @lc code=end
