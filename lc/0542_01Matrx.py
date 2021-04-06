# class Solution:
#     def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
#         from collections import deque
#         m = len(matrix)
#         n = len(matrix[0])
#         ans = [[0]*n for i in range(m)]
        
#         for i in range(m):
#             for j in range(n):
#                 q = deque()
#                 q.append((i,j,0))
#                 visited = set()
#                 visited.add((i,j))
#                 while q:
#                     r,c,dist = q.popleft()
#                     if matrix[r][c] == 0:
#                         ans[i][j] = dist
#                         break
#                     ## add neighbors
#                     for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
#                         if (r+dr,c+dc) not in visited and 0<=r+dr<m and 0<=c+dc<n:
#                             q.append((r+dr,c+dc,dist+1))
#                             visited.add((r+dr,c+dc))
#         return ans

class Solution:
    '''
    dp
    '''
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        from collections import deque
        m = len(matrix)
        n = len(matrix[0])
        ans = [[m+n]*n for i in range(m)] # initialize with max distance
        
        # 1st pass
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    ans[i][j] = 0
                else:
                    if i > 0:
                        ans[i][j] = min(ans[i][j], ans[i-1][j] + 1)
                    if j > 0:
                        ans[i][j] = min(ans[i][j], ans[i][j-1] + 1)
                        
        # 2nd pass
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if matrix[i][j] == 0:
                    ans[i][j] = 0
                else:
                    if i < m - 1:
                        ans[i][j] = min(ans[i][j], ans[i+1][j] + 1)
                    if j < n - 1:
                        ans[i][j] = min(ans[i][j], ans[i][j+1] + 1)
        return ans
    
    