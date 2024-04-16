'''
Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
Follow up:
What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?
'''
# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         len_nums = len(nums)
#         len_max = 0
#         len_current = 0
#         idx_zeros = [-1,-1]
        
#         for idx in range(len_nums+1):
#             if idx==len_nums:
#                 idx_zeros.append(idx)
#                 len_current = idx_zeros[-1]-idx_zeros[-3]-1
#                 len_max = len_current if len_current>len_max else len_max
#             elif nums[idx]==0:
#                 idx_zeros.append(idx)
#                 len_current = idx_zeros[-1]-idx_zeros[-3]-1
#                 len_max = len_current if len_current>len_max else len_max
#             else:
#                 pass
#         return len_max
                
# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         left = 0
#         right = 0
#         max_len = 0
#         tmp_len = 0
#         zero_counter = 0
#         K = 1
        
#         while right < len(nums):
#             if nums[right] == 0:
#                 zero_counter += 1
#             if zero_counter > K:
#                 left += 1
#                 if nums[left-1] == 0:
#                     zero_counter -= 1
#             else:
#                 tmp_len = right - left + 1
#                 if tmp_len > max_len:
#                     max_len = tmp_len
#             right += 1
                    
#         return max_len

## 12/18/2020
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # exceptions
        if nums==None:
            return None
        N = len(nums)
        if N==0:
            return 0
        elif N==1:
            return 1
        
        # start the counting
        left = 0
        right = 0
        zero_counter = 0
        max_len = 0
        current_len = 0
        
        while right<N:
            if nums[right]==0:
                zero_counter += 1
            if zero_counter <= 1:
                current_len = right - left + 1
                if current_len > max_len:
                    max_len = current_len
            else:
                if nums[left]==0:
                    zero_counter -= 1
                left += 1
            right += 1
        return max_len
