#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # build lookup
        lookup = {}
        for num in nums1:
            if num not in lookup:
                lookup[num] = 1
            else:
                lookup[num] += 1
        # verify
        output = []
        for num in nums2:
            if num in lookup and lookup[num]:
                output.append(num)
                lookup[num] -= 1
        return output


# @lc code=end

