class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        # exception
        if N<=2:
            return N
        
        j = 1
        counter = 1
        # traverse the list
        for i in range(1,N):
            if nums[i]==nums[i-1]:
                counter += 1
            else:
                counter = 1
            
            if counter <= 2:
                if i!=j:
                    nums[j] = nums[i]
                j += 1
        return j
        