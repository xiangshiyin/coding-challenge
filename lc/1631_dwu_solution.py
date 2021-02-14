class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        MAX = 10**6
        row = len(heights)
        col = len(heights[0])
        grid = []
        for i in range(0,row):
            grid.append([MAX]*col)
        grid[0][0]=0
        self._down_fill_grid(heights, grid)
        self._refill_grid(heights, grid)
        return grid[row-1][col-1]
        
        
    def _down_fill_grid(self,heights,grid):
        MAX = 10**6
        row = len(grid)
        col = len(grid[0])

        for j in range(1, col):
            left = max(abs(heights[0][j-1] - heights[0][j]), grid[0][j-1])
            grid[0][j] = left
        
        for i in range(1, row):
            up = max(abs(heights[i-1][0] - heights[i][0]),grid[i-1][0])
            grid[i][0] = up
            
        for i in range(1, row):
            for j in range(1,col):
                left = max(abs(heights[i][j-1] - heights[i][j]), grid[i][j-1])
                up = max(abs(heights[i-1][j] - heights[i][j]),grid[i-1][j])
                grid[i][j] = min(left,up)
        
    def _refill_grid(self,heights,grid):
        MAX = 10**6
        row = len(grid)
        col = len(grid[0])
        for i in range(0,row):
            for j in range(0,col):
                left = max(abs(heights[i][j-1] - heights[i][j]),grid[i][j-1]) if j > 0 else MAX
                up = max(abs(heights[i-1][j] - heights[i][j]), grid[i-1][j]) if i > 0 else MAX
                right = max(abs(heights[i][j+1] - heights[i][j]), grid[i][j+1]) if j < col - 1 else MAX
                down = max(abs(heights[i+1][j] - heights[i][j]), grid[i+1][j]) if i <row - 1 else MAX
                m = min([left,up,right,down])
                if m < grid[i][j]:
                    grid[i][j] = m
                    self._back_fill(heights, grid, i,j-1)
                    self._back_fill(heights, grid, i-1,j)
                    
    def _back_fill(self, heights, grid, i, j):
        if i < 0 or j < 0:
            return
        MAX = 10**6
        row = len(grid)
        if i >= row:
            return
        col = len(grid[0])
        if j >= col:
            return
        left = max(abs(heights[i][j-1] - heights[i][j]),grid[i][j-1]) if j > 0 else MAX
        up = max(abs(heights[i-1][j] - heights[i][j]), grid[i-1][j]) if i > 0 else MAX
        right = max(abs(heights[i][j+1] - heights[i][j]), grid[i][j+1]) if j < col - 1 else MAX
        down = max(abs(heights[i+1][j] - heights[i][j]), grid[i+1][j]) if i <row - 1 else MAX
        s = min([left,up,right,down])
        if s < grid[i][j]:
            grid[i][j] = s
            self._back_fill(heights, grid, i-1, j)
            self._back_fill(heights, grid, i, j - 1) 
            self._back_fill(heights, grid, i+1, j)
            self._back_fill(heights, grid, i, j+1)
        return
        