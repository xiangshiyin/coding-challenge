# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

# Example 1:
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# case: [-2,3,-4]

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if i==0:
                positive = nums[0]
                negative = nums[0]
                result = nums[0]
                print(positive, negative, result)
            else:
                # print(nums[i], positive*nums[i], negative*nums[i])
                max_temp = max(nums[i], positive*nums[i], negative*nums[i])
                min_temp = min(nums[i], positive*nums[i], negative*nums[i])
                positive = max_temp
                negative = min_temp
                result = max(positive, result)
                print(positive, negative, result)
        return(result)

