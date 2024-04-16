#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:

            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            if l == r and nums[l] != target:
                return -1

            if nums[l] > nums[mid]:
                if target < nums[mid]:
                    r = mid - 1
                elif target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target > nums[mid]:
                    l = mid + 1
                elif target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


# @lc code=end
