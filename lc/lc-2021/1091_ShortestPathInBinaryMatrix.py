class Solution:
    def valid(self, i, j):
        return (
            i >= 0
            and i < len(self.grid)
            and j >= 0
            and j < len(self.grid)
            and self.visited[i][j] == 0
            and self.grid[i][j] == 0
        )

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        BFS search from the upper left corner to lower right corner
        """
        self.grid = grid
        m = len(grid)
        self.visited = [[0] * m for i in range(m)]

        from collections import deque

        queue = deque()
        if grid[0][0] == 1 or grid[m - 1][m - 1] == 1:
            return -1

        queue.append((0, 0, 0))
        self.visited[0][0] = 1

        while queue:
            # pop
            i, j, step = queue.popleft()

            # evaluate
            if i == m - 1 and j == m - 1:
                return step + 1

            # add children
            if self.valid(i + 1, j + 1):
                queue.append((i + 1, j + 1, step + 1))
                self.visited[i + 1][j + 1] = 1
            if self.valid(i + 1, j):
                queue.append((i + 1, j, step + 1))
                self.visited[i + 1][j] = 1
            if self.valid(i, j + 1):
                queue.append((i, j + 1, step + 1))
                self.visited[i][j + 1] = 1
            if self.valid(i - 1, j):
                queue.append((i - 1, j, step + 1))
                self.visited[i - 1][j] = 1
            if self.valid(i, j - 1):
                queue.append((i, j - 1, step + 1))
                self.visited[i][j - 1] = 1
            if self.valid(i - 1, j - 1):
                queue.append((i - 1, j - 1, step + 1))
                self.visited[i - 1][j - 1] = 1
            if self.valid(i - 1, j + 1):
                queue.append((i - 1, j + 1, step + 1))
                self.visited[i - 1][j + 1] = 1
            if self.valid(i + 1, j - 1):
                queue.append((i + 1, j - 1, step + 1))
                self.visited[i + 1][j - 1] = 1
            # print(queue)
            # print(self.visited)
        return -1
