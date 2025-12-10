class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return -1
