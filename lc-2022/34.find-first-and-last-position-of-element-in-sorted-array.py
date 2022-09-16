#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
# solution on 2022-09-15
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target < nums[0] or target > nums[-1]:
            return [-1, -1]
        n = len(nums)
        l = 0
        r = n - 1
        output = [n, -1]
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                if nums[l] == target:
                    output[0] = min(output[0], l)
                    output[1] = max(output[1], l)
                if nums[r] == target:
                    output[0] = min(output[0], r)
                    output[1] = max(output[1], r)
                l += 1
                r -= 1

        if output == [n, -1]:
            return [-1, -1]
        elif output[0] == n:
            output[0] = output[1]
        elif output[1] == -1:
            output[1] = output[0]

        return output


# @lc code=end

