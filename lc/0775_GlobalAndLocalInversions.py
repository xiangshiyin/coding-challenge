# class Solution:
#     def isIdealPermutation(self, A: List[int]) -> bool:
#         n = len(A)
        
#         # 1st pass. traverse the list from right to left, record the min value to the right
#         min_vs = [A[n - 1] for i in range(n)]
#         for i in range(n-2, -1, -1):
#             min_vs[i] = min(A[i + 1], min_vs[i + 1])
#         print(min_vs)
        
#         # 2nd pass. validte if local equals global
#         for i in range(n-1):
#             if A[i] < A[i + 1] and A[i] > min_vs[i + 1]:
#                 return False
#             if A[i] > A[i + 1] and A[i] > min_vs[i + 1] and A[i + 1] != min_vs[i + 1]:
#                 return False
        
#         return True
    
        
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        n = len(A)
        cur_max = 0
        for i in range(n-2):
            cur_max = max(cur_max, A[i])
            if cur_max > A[i+2]:
                return False
            
        return True
                