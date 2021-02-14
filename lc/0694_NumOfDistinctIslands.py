class Solution:
    '''
    BFS solution
    '''
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # get the shape of the grid
        m = len(grid)
        n = len(grid[0])
        
        # define a log on visited grid points
        visited = [[0] * n for i in range(m)]
        # define a hash table to record the found islands
        islands = set()
        
        # BFS traversal and record visited islands
        from collections import deque
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0:
                    queue = deque([(i,j)]) # add the start point
                    island = []
                    while queue:
                        k,l = queue.popleft()
                        if visited[k][l] == 0 and grid[k][l] == 1:
                            # evaluate
                            island.append((k - i, l - j)) # accumulate the offsets

                            # mark visited points
                            visited[k][l] = 1

                            # add children
                            if k + 1 < m and grid[k + 1][l] == 1:
                                queue.append((k + 1, l))
                            if k - 1 >= 0 and grid[k - 1][l] == 1:
                                queue.append((k - 1, l))
                            if l + 1 < n and grid[k][l + 1] == 1:
                                queue.append((k, l + 1))
                            if l - 1 >= 0 and grid[k][l - 1] == 1:
                                queue.append((k, l - 1))
                    if len(island) > 0:   
                        islands.add(tuple(island))

                    # print((i,j), visited)
        
        return len(islands)
        
        