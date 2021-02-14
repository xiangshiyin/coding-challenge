# class Solution:
#     def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
#         from collections import deque
        
#         m = len(mat)
#         n = len(mat[0])
#         # step 1: get the diagonal elements and sort them
#         tb = {}
        
#         i = 0
#         while i < m:
#             j = 0
#             # collect the diagnoal elements
#             while j < n:
#                 if i - j not in tb:
#                     tb[i - j] = [mat[i][j]]
#                 else:
#                     tb[i - j].append(mat[i][j])
                
#                 # sort the list when it gets to the end
#                 if i == m - 1 or j == n - 1:
#                     tb[i - j] = deque(sorted(tb[i - j]))
                
#                 j += 1
            
#             i += 1
        
#         # print(tb)
#         # step 2: change the matrix cell values in place
#         for i in range(m):
#             for j in range(n):
#                 mat[i][j] = tb[i - j].popleft()
        
#         return mat


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        import heapq
        
        m = len(mat)
        n = len(mat[0])
        # step 1: get the diagonal elements and sort them
        tb = defaultdict(list)
        for i in range(m):
            for j in range(n):
                heapq.heappush(tb[i - j], mat[i][j])
        
        # step 2: change the matrix cell values in place
        for i in range(m):
            for j in range(n):
                mat[i][j] = heapq.heappop(tb[i - j])
        
        return mat

