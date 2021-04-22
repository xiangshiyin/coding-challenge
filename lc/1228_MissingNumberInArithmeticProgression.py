class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        return int((arr[0] + arr[n - 1]) * (n + 1) / 2) - sum(arr)
            
        
        