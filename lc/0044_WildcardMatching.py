class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = ' ' + s
        p = ' ' + p
        dp = [[0] * len(p) for i in range(len(s))]
        dp[0][0] = 1
        
        # initialize 1st row of dp
        for j in range(1, len(p)):
            if p[j] == '*':
                dp[0][j] = dp[0][j - 1] 
        
        # traverse the grids
        for i in range(1, len(s)):
            for j in range(1, len(p)):
                if s[i] == p[j] or p[j] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
        
        return dp[-1][-1]
        
    
    