# class Solution:
#     def reverse(self, nums: list, begin: int, end: int) -> None:
#         while begin<end:
#             nums[begin],nums[end] = nums[end],nums[begin]
#             begin, end = begin+1, end-1


#     def nextPermutation(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         N = len(nums)
#         if N>1:
#             i = N-1
#             j = N-1
#             while i>0:
#                 if nums[i]<=nums[i-1]:
#                     i -= 1
#                 else: # found the turning point
#                     ## find the slot and do the swap
#                     while j>=i:
#                         if nums[i-1]<nums[j]: # do the swap
#                             nums[j], nums[i-1] = nums[i-1], nums[j]
#                             break
#                         j -= 1
#                     break
#             ## reverse the section
#             if j>=i:
#                 self.reverse(nums, i, N-1)
#         return nums

# solution on 1/31/2021
class Solution:
    # utility function
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)

        # exception
        if N == 1:
            return nums

        i = N - 1
        while i > 0:
            if nums[i] <= nums[i - 1]:
                i -= 1
            else:
                j = N - 1
                while nums[i - 1] >= nums[j]:
                    j -= 1
                # swap
                nums[i - 1], nums[j] = nums[j], nums[i - 1]
                break

        # reverse the right hand side
        self.reverse(nums, i, N - 1)
