class Solution:
    def minDifference(self, nums: List[int]) -> int:
        '''
        Large numbers can become small, small numbers can become large
        
        '''
        
        # special cases
        if len(nums) <= 3:
            return 0
        
        # sort the list
        nums.sort()
        print(nums)
        
        return min(nums[-1] - nums[3], nums[-4] - nums[0], nums[-3] - nums[1], nums[-2] - nums[2])

        