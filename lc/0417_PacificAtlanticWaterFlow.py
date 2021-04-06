class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        '''
        DFS traversal from the pacific and atlantic ocean
        '''
        m = len(matrix)
        if m == 0:
            return []
        
        n = len(matrix[0])
        delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        p_visited = set()
        a_visited = set()
        
        def dfs(x, y, visited):
            visited.add((x, y))
            
            for dx,dy in delta:
                if 0 <= x + dx < m and 0 <= y + dy < n and (x + dx, y + dy) not in visited and matrix[x + dx][y + dy] >= matrix[x][y]:
                    dfs(x + dx, y + dy, visited)
        
        # left edge and right edge
        for i in range(m):
            dfs(i, 0, p_visited)
            dfs(i, n - 1, a_visited)
        
        # upper edge and lower edge
        for j in range(n):
            dfs(0, j, p_visited)
            dfs(m - 1, j, a_visited)
        
        return list(p_visited & a_visited)
        
        