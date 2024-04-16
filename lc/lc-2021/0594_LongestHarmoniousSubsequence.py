class Solution:
    def findLHS(self, nums: List[int]) -> int:
        N = len(nums)
        
        # exception
        if N == 1:
            return 0
        
        # create hash table on index
        tb = {}
        for num in nums:
            if num not in tb:
                tb[num] = 1
            else:
                tb[num] += 1
        
        # traverse the hash table
        max_len = 0
        for num in nums:
            if num + 1 in tb:
                max_len = max(max_len, tb[num] + tb[num + 1])
                
                
        return max_len
                    
                
                