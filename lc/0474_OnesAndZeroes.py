class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        '''
        dp, O(mn*len(str))
        '''
        dp = [[0]*(n+1) for i in range(m+1)]
        from collections import Counter
        
        ans = 0
        for v in strs:
            count = Counter(v)
            c0 = count['0']
            c1 = count['1']
            if c0 <= m and c1 <= n:
                for mx in range(m + 1 - c0)[::-1]:
                    for nx in range(n + 1 - c1)[::-1]:
                        if dp[mx][nx] > 0:
                            dp[mx + c0][nx + c1] = max(dp[mx + c0][nx + c1], dp[mx][nx] + 1)
                            ans = max(ans, dp[mx + c0][nx + c1])
                dp[c0][c1] = max(dp[c0][c1], 1) 
                ans = max(dp[c0][c1], ans)
                    
        return ans
    
    