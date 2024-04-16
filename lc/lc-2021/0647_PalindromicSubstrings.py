class Solution:
    def countSubstrings(self, s: str) -> int:
        self.counter = 0
        
        def helper(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                self.counter += 1
        
        for i in range(len(s)):
            
            # check the palindromic strings centered at i
            helper(s, i, i)
            
            # check the palindromic strings centered at (i, i + 1)
            helper(s, i, i + 1)
        
        return self.counter


# solution created on 3/27/2021
# # class Solution:
#     def countSubstrings(self, s: str) -> int:
#         n = len(s)
#         dp = [[0] * n for i in range(n)]
#         # initialize the diagonal elements
#         for i in range(n):
#             dp[i][i] = 1
        
#         # fill the blanks in dp
#         for i in range(n):
#             for j in range(i):
#                 if i - j == 1:
#                     dp[j][i] = 1 if s[j] == s[i] else 0
#                 else:
#                     dp[j][i] = 1 if dp[j + 1][i - 1] and s[j] == s[i] else 0
        
#         # sum up
#         counter = 0
#         for i in range(n):
#             for j in range(n):
#                 counter += dp[i][j]
        
#         return counter
                         
                    
# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         n = len(s)
#         dp = [[0] * n for i in range(n)]
#         # initialize the diagonal elements
#         for i in range(n):
#             dp[i][i] = 1
        
#         counter = n
#         # fill the blanks in dp
#         for i in range(n):
#             for j in range(i):
#                 if i - j == 1:
#                     dp[j][i] = 1 if s[j] == s[i] else 0
#                 else:
#                     dp[j][i] = 1 if dp[j + 1][i - 1] and s[j] == s[i] else 0
#                 counter += dp[j][i]
        
#         return counter        
            
            