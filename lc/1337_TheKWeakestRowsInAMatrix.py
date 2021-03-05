# class Solution:
#     def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
#         '''
#         sorted() function in python
#         '''
#         # create hash table to record # of soliders
#         soldiers = {i:sum(mat[i]) for i in range(len(mat))}
#         return sorted(soldiers, key = lambda x: (soldiers.get(x), x))[:k]
    
    
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        '''
        heapq.nsmallest
        '''    
        from heapq import nsmallest
        
        return [idx for s,idx in heapq.nsmallest(k, [(sum(mat[i]),i) for i in range(len(mat))])]
