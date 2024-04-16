'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         zero_counter = 0
#         for idx in range(len(nums)):
#             if nums[idx]==0:
#                 zero_counter += 1
#             else:
#                 if zero_counter > 0:
#                     nums[idx-zero_counter] = nums[idx]
#                     nums[idx] = 0


# solution as of 11/12/2021
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n==1:
            return nums
        
        # 1. count the zeros
        n0 = 0
        for i in range(n):
            if nums[i] == 0:
                n0 += 1
        
        if n0 == 0:
            return nums
        
        # 2. move the elements
        counter = 0
        for i in range(n):
            if nums[i]==0:
                counter += 1
            else:
                if counter > 0:
                    nums[i - counter] = nums[i]
                    nums[i] = 0
        return nums
            
# # solution as of 11/26/2021
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         if n == 1:
#             return nums
        
#         counter = 0
#         for i in range(n):
#             if nums[i] == 0:
#                 counter += 1
#             elif counter > 0:
#                 nums[i-counter] = nums[i]
#                 nums[i] = 0
        
#         return nums
        
        
        
def test(nums):
    print(nums)
    zero_counter = 0
    for idx in range(len(nums)):
        if nums[idx]==0:
            zero_counter += 1
        else:
            if zero_counter > 0:
                nums[idx-zero_counter] = nums[idx]
                nums[idx] = 0
        print(idx, zero_counter, nums)
    # print(nums)


if __name__ == "__main__":
    nums = [0,1,0,3,12]
    test(nums)
