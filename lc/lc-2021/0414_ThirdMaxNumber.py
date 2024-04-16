
# class Solution:
#     def thirdMax(self, nums: List[int]) -> int:
#         # exceptions
#         if nums==None:
#             return float('-inf')
#         N = len(nums)
#         if N==0:
#             return float('-inf')
        
#         # traverse the list
#         max_1st = nums[0]
#         max_2nd = None
#         max_3rd = None
        
#         for idx in range(1,N):
#             if nums[idx] > max_1st:
#                 max_3rd = max_2nd
#                 max_2nd = max_1st
#                 max_1st = nums[idx]
#             elif nums[idx] == max_1st:
#                 continue
#             elif max_2nd == None:
#                 max_2nd = nums[idx]
#             elif nums[idx] > max_2nd:
#                 max_3rd = max_2nd
#                 max_2nd = nums[idx]
#             elif nums[idx] == max_2nd:
#                 continue
#             elif max_3rd == None:
#                 max_3rd = nums[idx]
#             elif nums[idx] > max_3rd:
#                 max_3rd = nums[idx]
#             print(max_1st, max_2nd, max_3rd)
#         if max_3rd != None:    
#             return max_3rd
#         else:
#             return max_1st
        
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # exceptions
        if nums==None:
            return float('-inf') 
        if len(nums)==0:
            return float('-inf')
        
        # find the answer
        # Make a Set with the input.
        nums = set(nums)

        # Find the maximum.
        maximum = max(nums)

        # Check whether or not this is a case where
        # we need to return the *maximum*.
        if len(nums) < 3:
            return maximum

        # Otherwise, continue on to finding the third maximum.
        nums.remove(maximum)
        second_maximum = max(nums)
        nums.remove(second_maximum)
        return max(nums)        
