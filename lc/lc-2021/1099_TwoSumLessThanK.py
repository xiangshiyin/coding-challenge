# class Solution:
#     def twoSumLessThanK(self, nums: List[int], k: int) -> int:
#         N = len(nums)
#         if N<=1:
#             return -1
#         else:
#             nums2 = sorted(nums)
#             maxSum = -1
#             left = 0
#             right = N-1
#             while left<right:
#                 if nums2[left]+nums2[right]>=k:
#                     right -= 1
#                 else:
#                     maxSum = max(maxSum, nums2[left]+nums2[right])
#                     left += 1
#             return maxSum


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        N = len(nums)
        if N <= 1:
            return -1
        else:
            maxSum = -1
            # build a look up table
            tb = {}
            for num in nums:
                if num not in tb:
                    tb[num] = 1
                else:
                    tb[num] += 1
            # print(tb)
            # do the look up
            left = 1
            right = k - 2
            while left < right:
                # print(left, right)
                if left in tb and right in tb:
                    if left + right < k:
                        maxSum = max(maxSum, left + right)
                        left += 1
                        if tb[right] > 1 and 2 * right < k:
                            maxSum = max(maxSum, 2 * right)
                    else:
                        right -= 1
                        if tb[left] > 1 and 2 * left < k:
                            maxSum = max(maxSum, 2 * left)
                elif left in tb:
                    right -= 1
                    if tb[left] > 1 and 2 * left < k:
                        maxSum = max(maxSum, 2 * left)
                elif right in tb:
                    left += 1
                    if tb[right] > 1 and 2 * right < k:
                        maxSum = max(maxSum, 2 * right)
                else:
                    left += 1
                    right -= 1

            return maxSum
