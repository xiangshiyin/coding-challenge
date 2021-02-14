class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        '''
        brutal force
        '''
        if n<=1:
            return n
        
        nums = [0 for i in range(n+1)]
        maximum = 0
        
        for j in range(n+1):
            if j==1:
                nums[j] = 1
            else:
                if j%2==0:
                    nums[j] = nums[j//2]
                else:
                    nums[j] = nums[(j-1)//2] + nums[(j-1)//2 + 1]
            
            if j%2==1:
                maximum = max(maximum, nums[j])
        return maximum
    