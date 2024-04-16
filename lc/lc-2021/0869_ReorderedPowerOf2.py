# class Solution:
#     '''
#     Time limit exceeded
#     '''
#     def isPowerOf2(self, v):    
#         i = 1
#         while i <= v:
#             if i == v:
#                 return True
#             i = i << 1
#         return False
    
#     def swap(self, A, i, j):
#         tmp = A[i]
#         A[i] = A[j]
#         A[j] = tmp
        
#     def reorderedPowerOf2(self, N: int) -> bool:
#         # special cases
#         if self.isPowerOf2(N):
#             return True
        
#         # find all digits
#         ds = [] # all digits
#         v = N
        
#         while v > 0:
#             ds.append(v % 10)
#             v = v // 10
        
#         # try all permutations via dfs??
#         def dfs(ds, ix):
#             if ix == len(ds):
#                 if ds[0] == 0:
#                     return False
#                 else:
#                     v = 0
#                     for k in range(len(ds)):
#                         v += ds[len(ds) - 1 - k] * (10 ** k)
#                     return self.isPowerOf2(v)
#             for jx in range(ix, len(ds)):
#                 self.swap(ds, ix, jx) # swap
#                 if dfs(ds, ix + 1):
#                     return True
                
#                 self.swap(ds, ix, jx) # restore
            
#             return False
            
#         return dfs(ds, 0)    
            
        
class Solution:
    def getDigits(self, v):
        # find all digits
        ds = [] # all digits
        
        while v > 0:
            ds.append(v % 10)
            v = v // 10 
        
        from collections import Counter
        return Counter(ds)
        
    def reorderedPowerOf2(self, N: int) -> bool:
        '''
        2 ** 29 < 1e9 < 2 ** 30
        '''
        digits = self.getDigits(N)
        for i in range(30):
            if self.getDigits(2 ** i) == digits:
                return True
        return False
        
        
        
        
        