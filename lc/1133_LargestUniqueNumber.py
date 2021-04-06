class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        # exceptions
        n = len(A)
        if n == 1:
            return A[0]
        elif n == 2:
            return -1 if A[0]==A[1] else A[0]
        
        # sort the list
        A.sort(reverse=True)
        # print(A)
        
        # traverse the list until you find a value that's not repeated
        ix = 0
        while ix < n:
            if ix == 0 and A[ix] != A[ix+1]:
                return A[0]
            if ix < n - 1 and A[ix] != A[ix-1] and A[ix] != A[ix+1]:
                return A[ix]
            if ix == n - 1 and A[ix] != A[ix-1]:
                return A[ix]
            ix += 1
        return -1

# class Solution:
#     def largestUniqueNumber(self, A: List[int]) -> int:
#         '''
#         hash table
#         '''
#         from collections import Counter
#         tb = Counter(A)
#         # print(tb)
        
#         ans = -1
#         for v in tb:
#             if tb[v] == 1 and v > ans:
#                 ans = v
#         return ans


              