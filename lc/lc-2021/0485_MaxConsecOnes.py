"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""

## solution on 12/06/2020
# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         len_nums = len(nums) # length of the input list
#         zeros = [-1] # container for zero indexes
#         len_consec_max = 0 # maximum number of consecutive 1s
#         len_consec_current = 0 # recent number of consecutive 1s
#         for idx in range(len_nums+1):
#             if idx==len_nums:
#                 zeros.append(idx)
#                 len_consec_current = zeros[-1] - zeros[-2] - 1
#             elif nums[idx]==0:
#                 zeros.append(idx)
#                 len_consec_current = zeros[-1] - zeros[-2] - 1
#             else:
#                 pass
#             # update the maximum number of consecutive 1s
#             if len_consec_current>len_consec_max:
#                 len_consec_max = len_consec_current
#         return len_consec_max

# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         len_consec_max = 0 # maximum number of consecutive 1s
#         len_consec_current = 0 # recent number of consecutive 1s
#         for num in nums:
#             if num==1:
#                 len_consec_current += 1
#                 if len_consec_current>len_consec_max:
#                     len_consec_max = len_consec_current
#             else:
#                 len_consec_current = 0
#         return len_consec_max


## 12/18/2020
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # handle exceptions
        if nums == None:
            return None

        N = len(nums)
        if N == 0:
            return 0
        if N == 1:
            if nums[0] == 0:
                return 0
            else:
                return 1

        # do the counting
        max_len = 0
        current_len = 0
        for num in nums:
            if num == 1:
                current_len += 1
            else:
                if current_len > max_len:
                    max_len = current_len
                current_len = 0
        if current_len > max_len:
            max_len = current_len
        return max_len
