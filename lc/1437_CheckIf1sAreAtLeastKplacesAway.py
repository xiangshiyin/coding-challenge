class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        prev = -1
        curr = -1
        
        while curr < len(nums):
            if nums[curr] == 0:
                curr += 1
            else:
                if curr - prev - 1 < k and prev != -1:
                    return False
                else:
                    prev = curr
                curr += 1
        return True
            
            
        
        