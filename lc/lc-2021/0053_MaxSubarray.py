# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         # exceptions
#         if nums is None:
#             return None
#         N = len(nums)
#         if N==0:
#             return None
#         if N==1:
#             return nums[0]
        
#         # traverse the list
#         maxSum = nums[0]
#         tmpSum = nums[0]
        
#         for idx in range(1,N):
#             tmpSum = max(nums[idx], tmpSum+nums[idx])
#             maxSum = max(tmpSum, maxSum)
            
#         return maxSum

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # exceptions
        if nums is None:
            return None
        N = len(nums)
        if N==0:
            return None
        if N==1:
            return nums[0]        
        
        # traverse the list
        tmpSum = nums[0]
        maxSum = nums[0]
        
        for idx in range(1,N):
            if tmpSum<0:
                tmpSum = nums[idx]
            else:
                tmpSum += nums[idx]
            maxSum = max(maxSum, tmpSum)
        return maxSum
    
                
            
        