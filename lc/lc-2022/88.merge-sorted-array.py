#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m + n - 1
        lp = m - 1
        rp = n - 1
        while rp >= 0:
            if lp < 0 or nums2[rp] >= nums1[lp]:
                nums1[p] = nums2[rp]
                rp -= 1
            else:
                nums1[p] = nums1[lp]
                lp -= 1
            p -= 1


# @lc code=end
