class Solution:
    def longestValidParentheses(self, s: str) -> int:
        N = len(s)
        # exception
        if N<=1:
            return 0
        
        # traverse the string from right to left
        longest = 0
        lcounter = 0
        rcounter = 0
        marker = 0
        
        for i,char in enumerate(s):
            if char=='(':
                lcounter += 1
            else:
                rcounter += 1
            if rcounter > lcounter:
                longest = max(lcounter*2, longest)
                lcounter = 0 # clear ( counter
                rcounter = 0 # clear ) counter
                marker = i+1
        
        if lcounter==rcounter:
            longest = max(lcounter*2, longest)
        else:
            # traverse the section where redundant "(" might exist from right to left
            lcounter = 0
            rcounter = 0
            for j in range(N-1,marker-1,-1):
                if s[j]=='(':
                    lcounter += 1
                else:
                    rcounter += 1
                # print(lcounter, rcounter)
                if rcounter < lcounter:
                    longest = max(rcounter*2, longest)
                    lcounter = 0
                    rcounter = 0
            longest = max(rcounter*2, longest)
            
        
        return longest
                    
## solution on 4/3/2021
#  class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         n = len(s)
#         # exception
#         if n <= 1:
#             return 0
        
#         max_len = 0
#         # 1st pass, left to right
#         lcounter = 0
#         rcounter = 0
#         ix = 0
#         while ix < n:
#             if s[ix] == '(':
#                 lcounter += 1
#             else:
#                 rcounter += 1
#             if lcounter == rcounter:
#                 max_len = max(max_len, rcounter * 2)
#             elif lcounter < rcounter:
#                 lcounter = 0 
#                 rcounter = 0
#             ix += 1
            
#         # 2nd pass, right to left
#         lcounter = 0
#         rcounter = 0
#         ix = n - 1
#         while ix >= 0:
#             if s[ix] == '(':
#                 lcounter += 1
#             else:
#                 rcounter += 1
#             if lcounter == rcounter:
#                 max_len = max(max_len, rcounter * 2)
#             elif lcounter > rcounter:
#                 lcounter = 0 
#                 rcounter = 0
#             ix -= 1
            
#         return max_len

## solution on 4/3/2021
# class Solution:
#     '''
#     solution with stack and dp
#     '''
#     def longestValidParentheses(self, s: str) -> int:
#         n = len(s)
#         # exception
#         if n <= 1:
#             return 0

#         # traverse the string, update dp
#         dp = [0 for i in range(n+1)]
#         stack = []
#         ans = 0
        
#         for i in range(n):
#             if s[i] == '(':
#                 stack.append(i)
#             else:
#                 if stack:
#                     dp[i+1] = dp[stack[-1]] + i - stack[-1] + 1
#                     ans = max(ans, dp[i+1])
#                     stack.pop()
#                     # print(dp)
                    
#         return ans
    
                    
        
            