# class Solution:
#     def numDecodings(self, s: str) -> int:
#         '''
#         a number has 3 options to be decoded: 
#         1. be combined with left neighbor
#         2. be combined with right neighbor (can be counted in the right neighbor's counter)
#         3. decoded as is (single digits)
#         '''
#         n = len(s)
#         # exceptions
#         if s[0] == '0':
#             return 0
#         elif n == 1:
#             return 1
        
#         # dp traversal from left to right
#         dp = [0 for i in range(n)]
#         for i in range(n):
#             if i == 0:
#                 dp[i] = 1
#             else:
#                 if s[(i-1):(i+1)] > '26' or s[(i-1):(i+1)] < '10':
#                     if s[i] == '0':
#                         return 0
#                     else:
#                         dp[i] = dp[i - 1]
#                 else:
#                     if s[i] == '0':
#                         if i == 1:
#                             dp[i] = 1
#                         else:
#                             dp[i] = dp[i - 2]
#                     else:
#                         dp[i] = dp[i - 1] + dp[i - 2] if i > 1 else dp[i - 1] + 1            
#         # print(dp)
#         return dp[-1]


class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        DFS
        '''
        self.seen = {}
        
        def dfs(s, i):
            if i in self.seen:
                return self.seen[i]
            
            if i == len(s):
                return 1
            
            if s[i] == '0':
                return 0
            
            if i == len(s) - 1:
                return 1

            
            ans = dfs(s, i + 1)
            if '10' <= s[i:(i+2)] <= '26':
                ans += dfs(s, i + 2)
            
            self.seen[i] = ans
            
            return ans
            
        ans = dfs(s, 0)
        
        return ans
    
            
        
