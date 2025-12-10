#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         m = len(grid)
#         n = len(grid[0])
#         color = "2"
#         counter = 0

#         def dfs(grid, sr, sc, color):
#             m = len(grid)
#             n = len(grid[0])
#             drc = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#             # color the target
#             grid[sr][sc] = color
#             # flood the neighbors
#             for dr, dc in drc:
#                 if (
#                     0 <= sr + dr < m
#                     and 0 <= sc + dc < n
#                     and grid[sr + dr][sc + dc] == "1"
#                 ):
#                     dfs(grid, sr + dr, sc + dc, color)

#         for r in range(m):
#             for c in range(n):
#                 if grid[r][c] == "1":
#                     counter += 1
#                     dfs(grid, r, c, color)

#         return counter


# solution on 2022-09-17
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        drc = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visited = [[0] * n for i in range(m)]
        newColor = "2"

        def dfs(grid, r, c, newColor):
            grid[r][c] = newColor
            visited[r][c] = 1
            for dr, dc in drc:
                if (
                    0 <= r + dr < m
                    and 0 <= c + dc < n
                    and grid[r + dr][c + dc] == "1"
                    and visited[r + dr][c + dc] == 0
                ):
                    dfs(grid, r + dr, c + dc, newColor)

        counter = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    counter += 1
                    dfs(grid, r, c, newColor)

        return counter


# @lc code=end
