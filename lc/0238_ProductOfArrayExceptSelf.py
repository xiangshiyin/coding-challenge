# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i]
# Note: Please solve it without division and in O(n).

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1]
        right = 1
        ## going forward
        i = 1
        while i<len(nums):
            print(i, left[i-1]*nums[i-1])
            left.append(left[i-1]*nums[i-1])
            i += 1
               
        ## going backward
        j = len(nums)-1
        while j>=0:
            left[j] = right*left[j]
            right *= nums[j]
            j -= 1
        return(left)
