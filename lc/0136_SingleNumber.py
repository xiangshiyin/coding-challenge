# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         return 2 * sum(set(nums)) - sum(nums)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for num in nums:
            a ^= num
        return a
        