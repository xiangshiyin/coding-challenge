# class Solution:
#     def numberOfArithmeticSlices(self, A: List[int]) -> int:
#         '''
#         dp, O(n2), only beats 5%
#         '''
#         n = len(A)
        
#         # exception
#         if n < 3:
#             return 0
        
#         # create a grid for dp recording
#         grid = [[0]*n for i in range(n)]
#         counter = 0
#         for step in range(2, n):
#             for i in range(n - 2):
#                 if step == 2:
#                     grid[i][i + step] = 1 if A[i] - A[i + 1] == A[i + 1] - A[i + 2] else 0
#                 else:
#                     if i + step < n and i < n - 3:
#                         grid[i][i + step] = grid[i][i + step - 1] & grid[i + 1][i + step]
#                 if i < n - 2 and i + step < n:
#                     counter += grid[i][i + step]
        
#         return counter
        
# class Solution:
#     def numberOfArithmeticSlices(self, A: List[int]) -> int:
#         counter = 0
#         for i in range(len(A) - 2):
#             for j in range(i + 2, len(A)):
#                 if A[i] - A[i + 1] == A[j - 1] - A[j]:
#                     counter += 1
#                 else:
#                     break
#         return counter

# class Solution:
#     def numberOfArithmeticSlices(self, A: List[int]) -> int:
#         '''
#         dp with O(n) space
#         '''
#         n = len(A)
#         dp = [0 for i in range(n)]
#         counter = 0
#         for i in range(2, n):
#             if A[i] - A[i-1] == A[i-1] - A[i-2]:
#                 dp[i] = 1 + dp[i - 1]
#                 counter += dp[i]
        
#         return counter
    
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        '''
        dp with O(1) space
        '''
        n = len(A)
        prev = 0
        counter = 0
        for i in range(2, n):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                prev = 1 + prev
            else:
                prev = 0
                
            counter += prev
        
        return counter        
        