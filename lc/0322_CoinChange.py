# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         '''
#         BFS solution
#         '''
#         if amount == 0:
#             return 0
        
#         seen = set()
        
#         from collections import deque
#         q = deque([[0,0]])
        
#         while q:
#             curr,level = q.popleft()
            
#             if level != 0 and curr == amount:
#                 return level
            
#             for c in coins:
#                 if curr + c not in seen and curr + c <= amount:
#                     q.append([curr + c, level + 1])
#                     seen.add(curr + c)
#         return -1
                
        
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        dp, bottom up
        '''
        if amount == 0:
            return 0
        
        dp = [amount+1 for i in range(amount + 1)]
        dp[0] = 0
        
        for i in range(amount + 1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        
        return dp[amount] if dp[amount] != amount + 1 else -1
                
        
            
                    
        