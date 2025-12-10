"""
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s.



Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation:
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation:
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.


Note:

1 <= A.length <= 20000
0 <= K <= A.length
A[i] is 0 or 1
"""

# class Solution:
#     def longestOnes(self, A: List[int], K: int) -> int:
#         idx_zeros = [-1]*(K+1)
#         self.len_max = 0
#         len_current = 0
#         len_A = len(A)

#         for idx in range(len_A+1):
#             if idx==len_A:
#                 self.updateZeros(idx, idx_zeros, K)
#             elif A[idx]==0:
#                 self.updateZeros(idx, idx_zeros, K)
#             else:
#                 pass
#         return self.len_max


#     def updateZeros(self, idx, idx_zeros, K):
#         idx_zeros.append(idx)
#         len_current = idx_zeros[-1] - idx_zeros[-2-K] - 1
#         self.len_max = len_current if len_current>self.len_max else self.len_max


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = 0
        right = 0
        zero_counter = 0
        max_len = 0

        while right < len(A):
            if A[right] == 0:
                zero_counter += 1
            if zero_counter > K:
                left += 1
                if A[left - 1] == 0:
                    zero_counter -= 1
            else:
                tmp_len = right - left + 1
                if tmp_len > max_len:
                    max_len = tmp_len
            right += 1

        return max_len
