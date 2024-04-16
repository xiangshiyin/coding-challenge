class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        if m == 1 or n == 1:
            return 0
        
        # step 1: traverse the list and build lookup tables of 1s in each row
        tb = [
            set([j for j in range(n) if grid[i][j] == 1])
            for i in range(m)
        ]
        
        # step 2: traverse each row again, search corner rectangles
        counter = 0
        for i in range(1, m):
            if len(tb[i]) > 1:
                for j in range(i):
                    overlap = len(tb[j] & tb[i])
                    counter += overlap * (overlap - 1) // 2
        return counter
    