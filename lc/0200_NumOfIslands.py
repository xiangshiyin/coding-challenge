# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         '''
#         BFS search
#         '''
#         from collections import deque
#         visited = set()
#         counter = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == "1" and (i,j) not in visited:
#                     q = deque([(i, j)])
#                     visited.add((i,j))
#                     counter += 1
                    
#                     while q:
#                         k, l = q.popleft()
#                         for x, y in [[k + 1, l], [k - 1, l], [k, l + 1], [k, l - 1]]:
#                             if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1" and (x, y) not in visited:
#                                 q.append((x,y))
#                                 visited.add((x,y))
#         return counter


# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         '''
#         BFS search with in place marker
#         '''
#         from collections import deque
#         counter = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == "1":
#                     q = deque([(i, j)])
#                     grid[i][j] = "-1"
#                     counter += 1
                    
#                     while q:
#                         k, l = q.popleft()
#                         for x, y in [[k + 1, l], [k - 1, l], [k, l + 1], [k, l - 1]]:
#                             if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1":
#                                 q.append((x,y))
#                                 grid[x][y] = "-1"
        
#         return counter
    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        DFS search with in place marker
        '''
        m = len(grid)
        n = len(grid[0])
        # print(m, n)
        
        counter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1': # found a new island
                    counter += 1
                    q = [(i, j)]
                    grid[i][j] = '-1'
                    while q:
                        k, l = q.pop()
                        ## add all children
                        if k + 1 < m and l < n and grid[k + 1][l] == '1':
                            q.append((k + 1, l))
                            grid[k + 1][l] = '-1'
                        if k < m and l + 1 < n and grid[k][l + 1] == '1':
                            q.append((k, l + 1))
                            grid[k][l + 1] = '-1'
                        if k - 1 >= 0 and l < n and grid[k - 1][l] == '1':
                            q.append((k - 1, l))
                            grid[k - 1][l] = '-1'
                        if k < m and l - 1 >= 0 and grid[k][l - 1] == '1':
                            q.append((k, l - 1))
                            grid[k][l - 1] = '-1'
        return counter
        