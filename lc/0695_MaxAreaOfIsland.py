class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        bfs solution
        '''
        maxArea = 0
        m = len(grid)
        n = len(grid[0])
        
        from collections import deque
        drcs = [
            [0,1],
            [0,-1],
            [1,0],
            [-1,0]
        ]
        
        for r in range(m):
            for c in range(n):
                area = 0
                if grid[r][c] == 1:
                    q = deque([(r,c)])
                    while q:
                        sr, sc = q.popleft()
                        area += 1
                        grid[sr][sc] = 0
                        
                        for dr, dc in drcs:
                            if 0<=sr+dr<m and 0<=sc+dc<n and grid[sr+dr][sc+dc]==1:
                                q.append((sr+dr, sc+dc))
                                grid[sr+dr][sc+dc] = 0
                maxArea = max(maxArea, area)
        
        return maxArea
                    
