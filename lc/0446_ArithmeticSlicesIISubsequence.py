class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        '''
        dp with number of pairs recorded at each step
        '''
        n = len(A)
        # exceptions
        if n < 3:
            return 0
        
        counter = 0
        from collections import defaultdict
        dp = [defaultdict(int) for a in A]
        
        for i in range(n):
            for j in range(i):
                dp[i][A[i] - A[j]] += 1
                if A[i] - A[j] in dp[j]:
                    dp[i][A[i] - A[j]] += dp[j][A[i] - A[j]]
                    counter += dp[j][A[i] - A[j]]
        
        
        
        return counter
    
                
        
        
    
    