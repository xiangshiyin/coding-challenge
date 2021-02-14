class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        '''
        union find solution
        '''
        m = len(heights)
        n = len(heights[0])
        
        # exceptions
        if m == 1 and n == 1:
            return 0
        
        ids = [i for i in range(m * n)]
        sizes = [1 for i in range(m * n)]
        
        # define the union-find utility functions
        def root(a):
            while ids[a] != a:
                ids[a] = ids[ids[a]] # path compression
                a = ids[a]
            return a
        
        def union(a,b):
            ra = root(a)
            rb = root(b)
            if a == b: 
                return
            if sizes[ra] < sizes[rb]:
                ids[ra] = rb
                sizes[rb] += sizes[ra]
            else:
                ids[rb] = ra
                sizes[ra] += sizes[rb]
        
        # calculate all mutual height differences
        steps = []
        for i in range(1,m): # 1st row
            steps.append([(i-1)*n, i*n, abs(heights[i][0] - heights[i-1][0])])
        for j in range(1,n): # 1st col
            steps.append([j-1, j, abs(heights[0][j] - heights[0][j-1])])
        ## for the rest of interactions, only consider going down and going right
        for i in range(1,m):
            for j in range(1,n):
                # up -> down
                steps.append([(i-1)*n + j, i*n + j, abs(heights[i][j] - heights[i-1][j])])
                # left -> right
                steps.append([i*n + j - 1, i*n + j, abs(heights[i][j] - heights[i][j-1])])
        
        # sort the steps
        steps = sorted(steps, key = lambda x: x[2])
        
        # iterate through the sorted steps, build the path via union
        stop = 0
        while root(0) != root(m * n - 1):
            union(steps[stop][0], steps[stop][1])
            stop += 1
        
        if stop == 0:
            return steps[0][2]
        else:
            return steps[stop - 1][2]
        
        
                
        
        
        
        
        