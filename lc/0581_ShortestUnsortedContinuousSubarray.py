# class Solution:
#     def findUnsortedSubarray(self, nums: List[int]) -> int:
#         '''
#         dp
#         '''
#         n = len(nums)
        
#         # check local min values
#         min_vs = [nums[-1] for i in range(n)]
#         for i in range(n-2, -1, -1):
#             min_vs[i] = min(nums[i], min_vs[i + 1])
#         # print(min_vs)
        
#         # find the left boundary
#         l = 0
#         while l < n and nums[l] == min_vs[l]:
#             l += 1
#         # print(l)
        
#         if l < n - 1:
#             # check local max values
#             max_vs = [nums[l] for i in range(n)]
#             for i in range(l+1,n):
#                 max_vs[i] = max(nums[i], max_vs[i-1])
#             # print(max_vs)

#             # find the right boundary
#             r = n - 1
#             while r >= 0 and nums[r] == max_vs[r]:
#                 r -= 1
#             return r - l + 1
        
#         else:
#             return 0
        
        
# class Solution:
#     def findUnsortedSubarray(self, nums: List[int]) -> int:
#         '''
#         with stack
#         '''
#         n = len(nums)        
        
#         # find the left boundary
#         min_stack = []
#         l = n - 1
#         i = 0
#         while i < n:
#             while min_stack and nums[min_stack[-1]] > nums[i]:
#                 l = min(l, min_stack.pop())
#             min_stack.append(i)
#             i += 1
        
#         # find the right boundary
#         max_stack = []
#         r = 0
#         j = n - 1
#         while j >= 0:
#             while max_stack and nums[max_stack[-1]] < nums[j]:
#                 r = max(r, max_stack.pop())
#             max_stack.append(j)
#             j -= 1
        
        
#         if r > l:
#             return r - l + 1
#         else:
#             return 0
        
               
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        '''
        O(1) space?
        '''     
        n = len(nums)
        min_v = max(nums)
        max_v = min(nums)
        
        # find the 1st drop from left to right
        i = 0
        while i < n:
            while i < n - 1 and nums[i] <= nums[i + 1]:
                i += 1
            if i < n - 1:
                min_v = min(min_v, nums[i + 1])
            i += 1
            
        # find the 1st rise from right to left
        j = n - 1
        while j >= 0:
            while j > 0 and nums[j] >= nums[j - 1]:
                j -= 1

            if j > 0:
                max_v = max(max_v, nums[j - 1])
            j -= 1
        
        # find the correct position of min and max
        for l in range(n):
            if nums[l] > min_v:
                break
        
        for r in range(n - 1, -1, -1):
            if nums[r] < max_v:
                break
            
        if r > l:
            return r - l + 1
        else:
            return 0
        
        
        