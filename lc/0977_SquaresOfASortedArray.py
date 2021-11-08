# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         left = 0
#         right = len(nums)-1
#         output = []
        
#         while left <= right:
#             if nums[right]**2 > nums[left]**2:
#                 output.append(nums[right]**2)
#                 right -= 1
#             else:
#                 output.append(nums[left]**2)
#                 left += 1
        
#         output2 = [
#             output[i]
#             for i in range(len(output)-1, -1, -1)
#         ]
#         return output2
        
# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         '''
#         The in-place solution
#         '''
#         N = len(nums)
#         pos = 0
#         # exceptions
#         if nums==None:
#             return None
#         if nums==[]:
#             return []
#         if N==1:
#             return [nums[0]**2]
        
#         # initialize pos pointer
#         while pos<N and nums[pos]<0:
#             pos += 1
        
#         # initialize neg pointer
#         neg = pos - 1
#         # print(neg, pos)
        
#         # generating the output
#         ans = []
#         while neg>=0 and pos<=N-1:
#             if nums[neg]**2<nums[pos]**2:
#                 ans.append(nums[neg]**2)
#                 neg -= 1
#             else:
#                 ans.append(nums[pos]**2)
#                 pos +=1
#         while neg>=0:
#             ans.append(nums[neg]**2)
#             neg -= 1
#         while pos<=N-1:
#             ans.append(nums[pos]**2)
#             pos += 1
        
#         return ans

## as of 11/7/2021
# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         '''
#         Runtime: 2296 ms, faster than 5.00% of Python3 online submissions for Squares of a Sorted Array.
#         Memory Usage: 16.4 MB, less than 12.35% of Python3 online submissions for Squares of a Sorted Array.
#         '''
#         output = []
#         l = 0
#         r = len(nums) - 1
#         while l <= r:
#             if abs(nums[l]) > abs(nums[r]):
#                 output = [nums[l] ** 2] + output
#                 l += 1
#             else:
#                 output = [nums[r] ** 2] + output
#                 r -= 1
#         return output


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums) # place holder
        n = len(nums)
        l = 0
        r = n - 1
        for i in range(n - 1, -1 , -1):
            if abs(nums[l]) > abs(nums[r]):
                output[i] = nums[l] ** 2
                l += 1
            else:
                output[i] = nums[r] ** 2
                r -= 1
        return output
        
    
