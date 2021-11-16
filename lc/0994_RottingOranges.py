class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        bfs solution following guideline
        '''
        m = len(grid)
        n = len(grid[0])
        dist = [[m*n] * n for i in range(m)]
        
        from collections import deque
        q = deque()
        fresh = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2: # rotten
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        q.append((-1,-1)) # marker of the end of one round                    
        
        drcs = [[-1,0],[1,0],[0,1],[0,-1]]
        steps = -1
        
        while q:
            r, c = q.popleft()
            if r == -1: # end of one round
                steps += 1
                if q:
                    q.append((-1,-1))
            else:
                for dr,dc in drcs:
                    if 0<=r+dr<m and 0<=c+dc<n and grid[r+dr][c+dc]==1:
                        grid[r+dr][c+dc] = 2
                        fresh -= 1
                        q.append((r+dr, c+dc))
        
        if fresh == 0:
            return steps
        else:
            return -1
        
                
                        
                        
                        
                        
        
        
        
        
                
