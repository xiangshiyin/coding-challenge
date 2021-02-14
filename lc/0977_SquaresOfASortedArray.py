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
        
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
        The in-place solution
        '''
        N = len(nums)
        pos = 0
        # exceptions
        if nums==None:
            return None
        if nums==[]:
            return []
        if N==1:
            return [nums[0]**2]
        
        # initialize pos pointer
        while pos<N and nums[pos]<0:
            pos += 1
        
        # initialize neg pointer
        neg = pos - 1
        # print(neg, pos)
        
        # generating the output
        ans = []
        while neg>=0 and pos<=N-1:
            if nums[neg]**2<nums[pos]**2:
                ans.append(nums[neg]**2)
                neg -= 1
            else:
                ans.append(nums[pos]**2)
                pos +=1
        while neg>=0:
            ans.append(nums[neg]**2)
            neg -= 1
        while pos<=N-1:
            ans.append(nums[pos]**2)
            pos += 1
        
        return ans
    