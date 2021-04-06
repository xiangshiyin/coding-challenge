class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''
        dfs or dp??
        record numbers for visited grids
        '''
        m = len(matrix)
        n = len(matrix[0])
        delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = [[0] * n for i in range(m)]
        
        def dfs(x, y):
            curr = visited[x][y]
            for dx, dy in delta:
                if 0 <= x + dx < m and 0 <= y + dy < n and matrix[x + dx][y + dy] > matrix[x][y]:
                    if not visited[x + dx][y + dy]:
                        dfs(x + dx, y + dy)
                    curr = max(curr, visited[x + dx][y + dy] + 1)
            visited[x][y] = curr if curr else 1
        
        ans = 1
        for i in range(m):
            for j in range(n):
                dfs(i, j)
                ans = max(ans, visited[i][j])
        
        # print(visited)
        return ans
        
        